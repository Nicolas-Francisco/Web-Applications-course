#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import filetype
import hashlib
import os

MAX_FILE_SIZE = 10000 * 1000  # 10 MB

class Doctor:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_doctor(self, data):
        # procesar y guardar el archivo
        fileobj = data[5]
        filename = fileobj.filename

        if not filename:
            return -1

        # verificamos el tipo
        size = os.fstat(fileobj.file.fileno()).st_size
        if size > MAX_FILE_SIZE:
            return -1

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM archivo"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = 'media/' + hash_archivo
        open(file_path, 'wb').write(fileobj.file.read())

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if (tipo.mime != 'image/png') and (tipo.mime != 'image/jpg') and (tipo.mime != 'image/jpeg'):
            os.remove(file_path)
            return -1

        # guardamos la imagen en la db
        sql = """
            INSERT INTO archivo (nombre, path)
            VALUES (%s, %s)
        """
        self.cursor.execute(sql, (filename, hash_archivo))
        self.db.commit()  # id
        id_archivo = self.cursor.getlastrowid()

        # guardamos el resto en la db
        sql = '''
            INSERT INTO medico (nombre, experiencia, especialidad,  email, celular, foto) 
            VALUES (%s, %s, %s, %s, %s, %s)
                        '''
        self.cursor.execute(sql, (*data[0:5], id_archivo))  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos

        return 1

    def get_doctors(self):
        sql = f"""
            SELECT medico.nombre, medico.experiencia, medico.especialidad, medico.email, medico.celular, archivo.path
            FROM medico, archivo WHERE medico.foto = archivo.id
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall() # retornamos la data
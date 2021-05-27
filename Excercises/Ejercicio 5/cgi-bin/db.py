#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import os
import filetype


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
        fileitem = data[5]
        filename = fileitem.filename

        #codificamos el file en binario y dps a hex
        hash_file = hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = 'media/' + hash_file
        open(file_path, 'wb').write(fileitem.file.read())

        sql ='''
        INSERT INTO archivo(nombre, path)
        VALUES(%s, %s)
        '''
        self.cursor.execute(sql, (filename, hash_file))
        self.db.commit()
        file_id = self.cursor.getlastrowid()

        sql = '''
        INSERT INTO medico(nombre, experiencia, especialidad, email, celular, foto)
        VALUES(%s,%s,%s,%s,%s,%s)
        '''
        self.cursor.execute(sql, (*data[0:5], file_id))
        self.db.commit()

    def get_doctors(self):
        sql = f"""
            SELECT * FROM medico
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data


    def get_file(self, id):
        sql = f"""
            SELECT path FROM archivo where id={id}
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import hashlib
import os
import filetype

MAX_FILE_SIZE = 10000 * 1000  # 10 MB

class Avistamiento
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.db.cursor()

    def save_avistamiento(self, data):
        # procesar y guardar el archivo
        fileobj = data[10]
        filename = fileobj.filename

        if not filename:
            return -1

        # verificamos el tipo
        size = os.fstat(fileobj.file.fileno()).st_size
        if size > MAX_FILE_SIZE:
            return -1

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM "
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        # file_path = 'media/' + hash_archivo
        # open(file_path, 'wb').write(fileobj.file.read())

        # guardar datos en la base de datos

        self.cursor.execute(sql, (filename, hash_archivo))
        self.db.commit()  # id
        id_archivo = self.cursor.getlastrowid()

        # guardamos el resto en la db
        sql = """
                INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
        self.cursor.execute(sql, (*data[0:10], id_archivo))  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos

        return 1


    def get_last_five_avistamientos(self):
        sql = ''' 
        SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo 
        FROM avistamiento AV, detalle_avistamiento DA, comuna CO 
        WHERE DA.avistamiento_id = AV.id 
        AND AV.comuna_id=CO.id 
        ORDER BY DA.dia_hora 
        DESC LIMIT 5 
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall() # retornamos la data

    def get_avistamientos(self, pag=0):
        sql = ''' 
                SELECT id, comuna_id, dia_hora, sector, nombre, email, celular
                FROM avistamiento
                '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        ids_avistamientos = ([fila[0] for fila in data])
        count = []
        for id in ids_avistamientos:
            sql = ''' 
                    SELECT COUNT(*)
                    FROM detalle_avistamiento
                    WHERE avistamiento_id = {id}
                            
                            '''
            self.cursor.execute(sql)
            cantidad = self.cursor.fetchall()[0][0]
            count.append(cantidad)

        ids_comunas = ([fila[1] for fila in data])
        comunas = []
        for id in ids_comunas:
            sql = ''' 
                            SELECT nombre
                            FROM 'comuna'
                            WHERE 'id' = {id}

                                    '''
            self.cursor.execute(sql)
            comuna = self.cursor.fetchall()[0][0]
            comunas.append(comuna)

        elementos = pag*5
        data = (data[elementos:elementos + 5], count[elementos:elementos + 5],
                comunas[elementos:elementos + 5], len(data))
        return data

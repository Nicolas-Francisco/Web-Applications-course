#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import hashlib
import os
import filetype

MAX_FILE_SIZE = 10000 * 1000  # 10 MB

class Avistamiento:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_avistamiento(self, data):
        datosbase = data[0]

        now = datosbase[0]

        nombre_comuna = datosbase[2]
        sql = f"""
        SELECT id
        FROM comuna 
        WHERE nombre="{nombre_comuna}"
        """
        self.cursor.execute(sql)
        id_comuna = self.cursor.fetchall()[0][0]

        name = datosbase[4]
        email = datosbase[5]

        sector = datosbase[3]
        celular = datosbase[6]

        if sector == "" and celular == "":
            sql = """
            INSERT INTO avistamiento (comuna_id, dia_hora, nombre, email) 
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(sql, (id_comuna, now, name, email))
            self.db.commit()

        if sector == "" and not celular == "":
            sql = """
            INSERT INTO avistamiento (comuna_id, dia_hora, nombre, email, celular) 
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (id_comuna, now, name, email, celular))
            self.db.commit()

        if not sector == "" and celular == "":
            sql = """
            INSERT INTO avistamiento (comuna_id, dia_hora, nombre, email, sector) 
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (id_comuna, now, name, email, sector))
            self.db.commit()

        if not sector == "" and not celular == "":
            sql = """
            INSERT INTO avistamiento (comuna_id, dia_hora, nombre, email, celular, sector) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (id_comuna, now, name, email, celular, sector))
            self.db.commit()

        id_avistamiento = self.cursor.getlastrowid()

        parse_tipo = {"N": "No sé",
                      "I": "Insecto",
                      "A": "Arácnido",
                      "M": "Miriápodo"}
        parse_estado = {"N": "No sé",
                        "V": "Vivo",
                        "M": "Muerto"}

        ids_detalle = []
        # Si la cantidad de avistamientos registrados es solo uno
        # Entonces tomamos los datos de la única lista enviada
        if len(data) == 1:
            dias_avistamiento = datosbase[7]
            tipo_avistamiento = datosbase[8]
            estado_avistamiento = datosbase[9]

            dia = dias_avistamiento.value
            tipo = parse_tipo[tipo_avistamiento.value]
            estado = parse_estado[estado_avistamiento.value]
            sql = """
            INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id) 
            VALUES (%s, %s, %s, %s);
            """
            self.cursor.execute(sql, (dia, tipo, estado, id_avistamiento))
            self.db.commit()
            ids_detalle.append(self.cursor.getlastrowid())

            fotos = datosbase[10]

        # Si no, entonces tenemos más listas con más datos.
        else:
            fotos = []

            for i in range(1, len(data)):
                dia = data[i][0].value
                tipo = parse_tipo[data[i][1].value]
                estado = parse_estado[data[i][2].value]
                sql = """
                INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id) 
                VALUES (%s, %s, %s, %s);
                """
                self.cursor.execute(sql, (dia, tipo, estado, id_avistamiento))
                self.db.commit()
                ids_detalle.append(self.cursor.getlastrowid())

                fotos.append(data[i][3])

        # Agregamos todas las fotos subidas
        print(ids_detalle)
        for i in range(len(fotos)):
            for j in range(len(fotos[i])):
                fileobj = fotos[i][j]
                filename = fileobj.filename
                id_detalle = ids_detalle[i]

                # calculamos cuantos elementos existen y actualizamos el hash
                sql = "SELECT COUNT(id) FROM foto"
                self.cursor.execute(sql)
                total = self.cursor.fetchall()[0][0] + 1
                hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

                # guardar el archivo
                file_path = 'media/' + hash_archivo
                open(file_path, 'wb').write(fileobj.file.read())

                sql = """
                INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id)
                VALUES (%s, %s, %s)
                """
                self.cursor.execute(sql, (hash_archivo, filename, id_detalle))
                self.db.commit()  # id
        return 1

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
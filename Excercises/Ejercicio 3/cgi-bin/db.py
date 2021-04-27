#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

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
        sql = '''
                    INSERT INTO doctors (nombre, experiencia, especialidad, email , celular) 
                    VALUES (%s, %s, %s, %s, %s)
                '''
        self.cursor.execute(sql, data)  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos

    def get_doctors(self):
        sql = f"""
            SELECT * FROM {doctors}
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall() # retornamos la data
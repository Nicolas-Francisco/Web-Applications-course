#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

db = mysql.connector.connect(
  host="localhost",       # 127.0.0.1
  user="root",
  password="",
  database="ejercicio3"
)

cursor = db.cursor()

cursor.execute('''
        CREATE TABLE doctors (
            id int(10) unsigned NOT NULL AUTO_INCREMENT,
            nombre VARCHAR(255), 
            experiencia TEXT(1000),
            especialidad VARCHAR(255), 
            email VARCHAR(255), 
            celular INTEGER,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
    ''')

print("La tabla se creo con éxito!")
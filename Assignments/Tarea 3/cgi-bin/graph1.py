#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import mysql.connector

connector = mysql.connector.connect(host="localhost", user="cc500258_u", password="uereturpis", database="cc500258_db")
cursor = connector.cursor()
print("Content-type: text/html; charset=UTF-8")
print('')

sql = "SELECT Count(*) FROM detalle_avistamiento WHERE tipo = 'arácnido' "
cursor.execute(sql)

aracnidos = cursor.fetchall()[0][0]

sql = "SELECT Count(*) FROM detalle_avistamiento WHERE tipo = 'miriápodo' "
cursor.execute(sql)

miriapodos = cursor.fetchall()[0][0]

sql = "SELECT Count(*) FROM detalle_avistamiento WHERE tipo = 'insecto' "
cursor.execute(sql)

insectos = cursor.fetchall()[0][0]

sql = "SELECT Count(*) FROM detalle_avistamiento WHERE tipo = 'no sé' "
cursor.execute(sql)

nose = cursor.fetchall()[0][0]

cantidad = {'Arácnidos': aracnidos, 'Miriápodos': miriapodos, 'Insectos': insectos, 'Desconocido': nose}

json.dumps(cantidad)
print(json.dumps(cantidad))  # Es necesario para que aparezca en el html
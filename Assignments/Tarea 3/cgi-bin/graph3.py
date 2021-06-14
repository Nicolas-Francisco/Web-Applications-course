#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import mysql.connector
import datetime
import calendar

connector = mysql.connector.connect(host="localhost", user="cc500258_u", password="uereturpis", database="cc500258_db")

cursor = connector.cursor()
print("Content-type: text/html; charset=UTF-8")
print('')


def Nombre_dia(fecha):
    dato = datetime.datetime.strptime(fecha, '%d %m %Y').weekday()
    return calendar.day_name[dato]


sql = "SELECT ALL dia_hora FROM detalle_avistamiento"
cursor.execute(sql)

fechas = cursor.fetchall()

diccionario_dias = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0,
                    'Friday': 0, 'Saturday': 0, 'Sunday': 0}

for fecha in fechas:
    dia = fecha[0].strftime('%d %m %Y')
    nombre_dia = Nombre_dia(dia)
    diccionario_dias[nombre_dia] += 1

json.dumps(diccionario_dias)
print(json.dumps(diccionario_dias))

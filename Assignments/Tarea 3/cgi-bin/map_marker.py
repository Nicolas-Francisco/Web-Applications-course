#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb;
import cgi
cgitb.enable()
import db
import json

database = db.Avistamiento("localhost", "cc500258_u", "uereturpis", "cc500258_db")
print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

nombre_comuna = cgi.FieldStorage()
listado_comuna = database.get_listado_comuna(nombre_comuna.getvalue('comuna'))

n = 0
diccionario_marcador = {}
for comuna in listado_comuna:
    diccionario_marcador[n] = [comuna[0].strftime("%d/%m/%Y %H:%M"), comuna[1], comuna[2], comuna[3], comuna[4]]
    n += 1

print(json.dumps(diccionario_marcador))
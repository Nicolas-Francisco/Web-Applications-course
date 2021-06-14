#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb;

cgitb.enable()
import db
import json

latitudes = None
with open("../latitud-longitud.json") as file:
    latitudes = json.load(file)

database = db.Avistamiento("localhost", "cc500258_u", "uereturpis", "cc500258_db")
print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

def get_comuna(nombre):
    for i in range(len(latitudes)):
        comuna = latitudes[i]
        nombre_comuna = comuna["name"]

        if (nombre_comuna==nombre):
            return comuna
    return ""

comunas_fotos = database.get_comunas_fotos()
diccionario_latitudes = {}

for comuna in comunas_fotos:
    datos_comuna = get_comuna(comuna[1])
    diccionario_latitudes[comuna[1]] = [datos_comuna["lat"], datos_comuna["lng"], comuna[2]]

print(json.dumps(diccionario_latitudes))

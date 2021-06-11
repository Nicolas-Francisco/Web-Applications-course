import json
import mysql.connector
import datatime
import calendar

connector = mysql.connector.connect(host="localhost", user="root", password="", database="tarea2")

cursor = connector.cursor()
print("Content-type: text/html; charset=UTF-8")
print('')

def Dia(fecha):
    dato = datatime.datetime.strptime(fecha, '%d %m %Y').weekday()
    return (calendar.day_name[dato])

sql = "SELECT ALL dia_hora FROM detalle_avistamiento"
cursor.execute(sql)

fechas = cursor.fetchall()

diccionario_dias = {'Lunes': 0, 'Martes': 0, 'Miercoles': 0, 'Jueves': 0,
                    'Viernes': 0, 'Sábado': 0, 'Domingo': 0}

for fecha in fechas:
    dia = d[0].strftime('%d %m %Y')
    nombre_dia = Dia(dia)
    diccionario_dias[nombre_dia] += 1

json.dumps(diccionario_dias)
print(json.dumps(diccionario_dias))
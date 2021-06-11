import json
import mysql.connector

connector = mysql.connector.connect(host="localhost", user="root", password="", database="tarea2")

cursor = connector.cursor()
print("Content-type: text/html; charset=UTF-8")
print('')

sql = "SELECT ALL dia_hora FROM detalle_avistamiento WHERE estado = 'vivo' "
cursor.execute(sql)

diccionario_vivos = {'01': 0, '02': 0, '03': 0, '04': 0,
                     '05': 0, '06': 0, '07': 0, '08': 0,
                     '09': 0, '10': 0, '11': 0, '12': 0}

fechas = cursor.fetchall()
for fecha in fechas:
    mes = fecha[0].strftime('%d/%m/%Y %H:%M:%S')
    diccionario_vivos[mes[3:5]] += 1  # Contador de vivos por mes


sql = "SELECT ALL dia_hora FROM detalle_avistamiento WHERE estado = 'muerto' "
cursor.execute(sql)

diccionario_muertos = {'01': 0, '02': 0, '03': 0, '04': 0,
                       '05': 0, '06': 0, '07': 0, '08': 0,
                       '09': 0, '10': 0, '11': 0, '12': 0}

fechas = cursor.fetchall()
for fecha in fechas:
    mes = fecha[0].strftime('%d/%m/%Y %H:%M:%S')
    diccionario_muertos[mes[3:5]] += 1  # Contador de muertos por mes


sql = "SELECT ALL dia_hora FROM detalle_avistamiento WHERE estado = 'no sé' "
cursor.execute(sql)

diccionario_nose = {'01': 0, '02': 0, '03': 0, '04': 0,
                    '05': 0, '06': 0, '07': 0, '08': 0,
                    '09': 0, '10': 0, '11': 0, '12': 0}

fechas = cursor.fetchall()
for fecha in fechas:
    mes = fecha[0].strftime('%d/%m/%Y %H:%M:%S')
    diccionario_nose[mes[3:5]] += 1  # Contador de estado 'no se' por mes


data = {'vivos': diccionario_vivos, 'muertos': diccionario_muertos, 'desconocido': diccionario_nose}
json.dumps(data)
print(json.dumps(data))  # Es necesario para que aparezca en el html
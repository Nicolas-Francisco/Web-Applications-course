import json
import mysql.connector

connector = mysql.connector.connect(host="localhost", user="root", password="", database="tarea2")

cursor = connector.cursor()
print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

sql = "SELEC Count(*) FROM detalle_avistamiento WHERE tipo = 'arácnido' "
cursor.execute(sql)

aracnidos = cursor.fetchall()[0][0]

sql = "SELEC Count(*) FROM detalle_avistamiento WHERE tipo = 'miriápodo' "
cursor.execute(sql)

miriapodos = cursor.fetchall()[0][0]

sql = "SELEC Count(*) FROM detalle_avistamiento WHERE tipo = 'insecto' "
cursor.execute(sql)

insectos = cursor.fetchall()[0][0]

sql = "SELEC Count(*) FROM detalle_avistamiento WHERE tipo = 'no sé' "
cursor.execute(sql)

nose = cursor.fetchall()[0][0]

cantidad = {'arácnidos':aracnidos, 'miriápodos':miriapodos, 'insectos':insectos, 'desconocido':nose}

json.dumps(cantidad)
print(json.dumps(cantidad)) # Es necesario para que aparezca en el html

cursor.close()
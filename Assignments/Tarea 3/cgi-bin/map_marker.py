import cgitb;
import cgi
cgitb.enable()
import db
import json

database = db.Avistamiento("localhost", "root", "", "tarea2")
print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

nombre_comuna = cgi.FieldStorage()
listado_comuna = database.get_listado_comuna(nombre_comuna.getvalue('comuna'))
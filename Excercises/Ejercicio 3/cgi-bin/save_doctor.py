#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
from db import Doctor

print("Content-type: text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
doctordb = Doctor("localhost", "root", "", "ejercicio3")

data = (
    form['nombre-medico'].value, form['experiencia-medico'].value, form['especialidad-medico'].value,
    form['email-medico'].value, form['celular-medico'].value
)
doctordb.save_doctor(data)

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio 3 </title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen"  href="style.css" />    <!-- CSS: -->
    <script src="jquery-3.5.0.js"></script>  <!-- Importing JQUERY  -->
</head>

<body>

<div>
    <!-- Body of page -->
    <h1> Datos de medico ingresados correctamente </h1>
</div>

</body>

"""

print(html)
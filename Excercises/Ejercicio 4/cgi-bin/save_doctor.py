#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
from db import Doctor

print("Content-type: text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
doctordb = Doctor("localhost", "root", "", "ejercicio4")

data = (
    form['nombre-medico'].value, form['experiencia-medico'].value, form['especialidad-medico'].value,
     form['email-medico'].value, form['celular-medico'].value,form['foto-medico']
)

html1 = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio 4 </title> <!-- Title in pestaña -->
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

html2 = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio 4 </title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen"  href="style.css" />    <!-- CSS: -->
    <script src="jquery-3.5.0.js"></script>  <!-- Importing JQUERY  -->
</head>

<body>

<div>
    <!-- Body of page -->
    <h1> Hubo un error al ingresar los datos, intente nuevamente </h1>
</div>



</body>

"""

if doctordb.save_doctor(data) == 1:
    print(html1)
else:
    print(html2)
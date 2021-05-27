#!/usr/bin/python3
# -*- coding: utf-8 -*-

from db import Doctor

print("Content-type: text/html\r\n\r\n")

doctordb = Doctor("localhost", "root", "", "ejercicio5")  #database del doctor
data = doctordb.get_doctors() #tenemos la data

html = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio 5 </title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen"  href="../style.css" />    <!-- CSS: -->
    <!--script src="jquery-3.5.0.js"></script-->  <!-- Importing JQUERY  -->
    <script src="../ajax.js"></script>  <!-- Importing JQUERY  -->
</head>
<body>

<ul class="topnav">
  <li><a class="active" href="../index.html">Inicio</a></li>
  <li><a href="../add_doctor.html">Agregar Datos de Médico</a></li>
  <li><a href="ajax_list.py">Ver Médicos</a></li>
</ul>

<div id="data">
<button type='button' onclick="ajaxList()"> Ver Datos </button>
</div>

</body>

</html>
'''

print(html)
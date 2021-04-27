#!/usr/bin/python3
# -*- coding: utf-8 -*-

from db import Doctor

print("Content-type:text/html\r\n\r\n")

doctordb = Doctor("localhost", "root", "", "ejercicio3")
data = doctordb.get_doctors('medico')

head = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio 2 </title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen"  href="style.css" />    <!-- CSS: -->
    <script src="jquery-3.5.0.js"></script>  <!-- Importing JQUERY  -->
</head>

<body>
<div>
    <!-- Body of page -->
    <h1>Datos de medico ingresados correctamente</h1>
</div>
<div>
    <table>
    <tr>
        <th>Nombre</th>
        <th>Experiencia</th>
        <th>Especialidad </th>
        <th>E-Mail </th>
        <th>Celular </th>
    </tr>
"""
print(head)
print(body)

for d in data:
    row = f'''
            <tr>
                <th>{str(d[1])}</th>
                <th>{str(d[2])}</th>
                <th>{str(d[3])}</th>
                <th>{str(d[5])}</th>
                <th>{str(d[6])}</th>
            </tr>
        '''
    print(row)

footer = f"""
    </table>
</div>

</body>

"""
print(footer)
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb

cgitb.enable()

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

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
"""
body = f"""
<body>

<div>
    <!-- Body of page -->
    <h1>Datos de médico ingresados correctamente</h1>
"""

footer = f"""

</div>


</body>

"""
form = cgi.FieldStorage()
print(head, file=utf8stdout)

print(body, file=utf8stdout)



for key in form.keys():
    print("<p>" + key+": "+form[key].value + "</p>", file=utf8stdout)



print(footer, file=utf8stdout)
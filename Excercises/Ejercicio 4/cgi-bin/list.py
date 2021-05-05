#!/usr/bin/python3
# -*- coding: utf-8 -*-

from db import Doctor

print("Content-type:text/html\r\n\r\n")

doctordb = Doctor("localhost", "root", "", "ejercicio4")
data = doctordb.get_doctors()

head = '''
<!DOCTYPE html>
<!--suppress ALL -->
<head>
    <meta charset="UTF-8">
    <title>ejercicio4</title>

</head>
'''

body1 = """
<body>
<div>
    <!-- Body of page -->
    <h1> Datos de medicos</h1>
</div>
<div>
    <table>
    <tr>
        <th>Nombre</th>
        <th>Experiencia</th>
        <th>Especialidad </th>
        <th>E-Mail </th>
        <th>Celular </th>
        <th>Foto </th>
    </tr>
"""

body2 = """
<body>
<div>
    <!-- Body of page -->
    <h1> Datos de medicos </h1>
    
    <h2> No hay médicos registrados </h2>
</div>
<div>
"""

if (len(data) != 0):
    print(body1)
    for d in data:
        row = f'''
                <tr>
                    <th>{str(d[0])}</th>
                    <th>{str(d[1])}</th>
                    <th>{str(d[2])}</th>
                    <th>{str(d[3])}</th>
                    <th>{str(d[4])}</th>
                    <th><img class="size" src=../media/{str(d[5])} width="120px" height="120px"></th>
                </tr>
            '''
        print(row)

    print("""
    </table>
    """)
else:
    print(body2)

footer = f"""
</div>

</body>
"""

print(footer)
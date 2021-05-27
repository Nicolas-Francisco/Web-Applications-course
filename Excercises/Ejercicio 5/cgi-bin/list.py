#!/usr/bin/python3
# -*- coding: utf-8 -*-

from db import Doctor

print("Content-type: text/html\r\n\r\n")

doctordb = Doctor("localhost", "root", "", "ejercicio5")  #database del doctor
data = doctordb.get_doctors() #tenemos la data



head = '''
    <!DOCTYPE html>
<!--suppress ALL -->
<head>
    <meta charset="UTF-8">
    <title> Listado Doctores </title>
    <link rel="stylesheet" type="text/css" href="../style.css">
    <script src="validador.js"></script>
    <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

.foto{
width: 120px;
height: 120px;
}
</style>
</head>
'''

print(head)
tableHTML = '''
<div class="main" style="margin-top: 3%">
        <table>
        <tr>
    <th>Nombre </th>
    <th>Experiencia</th>
    <th>Especialidad</th>
    <th>Foto</th>
    <th>Mail </th>
    <th>telefono </th>
'''
print(tableHTML)

if len(data) != 0:
    for d in data:

        img_name = doctordb.get_file(d[4])[0][0]
        #print(img_name)
        row = f'''
                <tr>
                    <th>{str(d[1])}</th>
                    <th>{str(d[2])}</th>
                    <th>{str(d[3])}</th>
                    <th>{str(d[5])}</th>
                    <th>{str(d[6])}</th>
                    <th> <img class="foto" alt="abeja para la pagina" src="../media/{str(img_name)}"> </th>
                </tr>
        '''

        print(row)
else:
    nodata = '''
    <h2>NO HAY MEDICOS EN EL REGISTRO</h2>
    '''
    print(nodata)

b2 = '''
</table>

</div>

</body>


</html>
'''
print(b2)



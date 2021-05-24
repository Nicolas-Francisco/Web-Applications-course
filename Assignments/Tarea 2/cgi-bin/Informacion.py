#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
import db

print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

pag = cgi.FieldStorage().getfirst("pag")
id_avist = cgi.FieldStorage().getfirst("id")

database = db.Avistamiento("localhost", "root", "", "tarea2")
data = database.get_avist(int(id_avist))

head = '''
<!DOCTYPE html>
<html lang="en">
    <meta charset="UTF-8">
    <title> RegistroBichos </title>
    <link rel="shortcut icon" href="img/emoji.ico" />
    <style>
        /* Body of the page*/
        body {
            font-family: Helvetica, sans-serif;
            margin: 0px;
        }
        .title {
            /* Title settings */
            text-align: center;
            font-size: 45px;
            margin-top: 2%;
            margin-bottom: 2%;
            color: #0CA200;
        }
        .subtitle {
            /* Subtitle settings */
            text-align: center;
            margin-top: 2%;
            font-size: 19px;
            color: black;
            background-color: #AAFF8F;
            padding-top: 15px;
        }
        .subsubtitle{
            /* Subtitle settings */
            width: 400px;
            background-color: #AAFF8F;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            border-top: 15px;
            border-bottom: 15px;
            margin: auto;
            font-size: 19px;
            color: black;
        }
        .jump{
            margin-top: 2%;
        }
        @media screen and (max-width: 500px){
            .black {
                font-size: 15px;
            }
        }
        .button {
            font-size: 15px;
            background-color: #AAFF8F;
            color: black;
            border: 2px solid #AAFF8F;
            border-radius: 6px;
            padding: 15px 30px;
            transition-duration: 0.2s;
            cursor: pointer;
            text-decoration: none;
            text-transform: uppercase;
        }
        .button:hover {
            background-color: white;
            color: #0CA200;
        }
        .leyenda {
            text-align: center;
            font-size: 15px;
        }
        .info {
            padding-top: 2%;
            font-family: Helvetica, sans-serif;
            margin: auto;
            text-align-all: center;
        }
        input {
            padding: 5px;
            width: 90%;
        }
        table {
            margin: auto;
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            text-align: center;
            border: 1px solid black;
        }
    </style>
    </head>
    '''

body1 = '''
<!-- RegistroBichos body -->
<body>

<div class="title"> RegistroBichos.com </div>

<div class="subtitle">
    Bienvenidos a RegistroBichos.com, la página de registro de avistamientos de insectos,
    arácnidos y miriápodos

    <br>

    <p class="leyenda">
        <a href="../informar.html"> 
        <button class="button"> Informar avistamiento </button> 
        </a>

        <a href="avistamientos.py?pag=1" >
            <button class="button" > Registro de Avistamientos </button>
        </a>
        <a href="../stats.html" >
            <button class="button"> Estadísticas </button>
        </a>
    <p>
</div>

<div class="jump"></div>

<div class="subsubtitle"> Datos de Avistamiento </div>
'''

print(head, file=utf8stdout)
print(body1, file=utf8stdout)

body2 = f'''
<div class="info">
    <div class="leyenda">
        <!-- We start a table to organize the info menu -->
        <table class="table">
            <!-- First row -->
            <tr>
                <td> Fecha/Hora </td>
                <td> {str(data[0])} </td>
            </tr>

            <!-- Second row -->
            <tr>
                <td> Comuna </td>
                <td> {str(data[1])} </td>
            </tr>

            <!-- Third row -->
            <tr>
                <td> Sector </td>
                <td> {str(data[2])} </td>
            </tr>

            <!-- Fourth row -->
            <tr>
                <td> Contacto </td>
                <td> {str(data[3])} - {str(data[4])} - {str(data[5])} </td>
            </tr>

            <!-- Fifth row -->
            <tr>
                <td> Tipo </td>
                <td> {str(data[6])} </td>
            </tr>

            <!-- Sixth row -->
            <tr>
                <td> Estado </td>
                <td> {str(data[7])} </td>
            </tr>
            <!-- Sixth row -->
            <tr>
                <td> Fotos </td>
                <td> {str(data[8])} </td>
            </tr>
        </table>
        <!-- We close the table -->
    </div>

    <div class="jump"></div>
'''

print(body2, file=utf8stdout)

for ruta in data[9]:
    row = f'''
    <div class="leyenda">
        <img src=../media/{ruta} height="240" width="320" id={ruta} alt="{ruta}">
    </div>

    <div class="leyenda">
        <button class="button" type="button" id="{ruta}-button" onclick="pop({ruta}, "{ruta}-button")"> Agrandar Imagen </button>
    </div> '''
    print(row, file=utf8stdout)


foot = '''
</div>

<div class="jump"></div>

<script>
    function pop(id, id_button){
        let imagen = document.getElementById(id);
        let boton = document.getElementById(id_button);
        imagen.setAttribute('height', '600');
        imagen.setAttribute('width', '800');
        boton.setAttribute('onclick', "closePop('insecto_js', 'insecto_js-button')");
    }

    function closePop(id, id_button){
        let imagen = document.getElementById(id);
        let boton = document.getElementById(id_button);
        imagen.setAttribute('height', '240');
        imagen.setAttribute('width', '320');
        boton.setAttribute('onclick', "pop('insecto_js', 'insecto_js-button')");
    }

</script>

</body>

</html>
'''

print(foot, file=utf8stdout)
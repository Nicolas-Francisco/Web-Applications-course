#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()

import db
from datetime import datetime

print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
database = db.Avistamiento("localhost", "root", "", "tarea2")

fotos = []
hayfotos = False
listavacia = True
listatemporal = []

for i in form.list:
    # Si el nombre del form es de una foto, entonces hay una foto
    if i.name == 'foto-avistamiento':
        hayfotos = True
    else:
        hayfotos = False

    # Si hay una foto, entonces lo guardamos temporalmente
    if hayfotos:
        listatemporal.append(i)
        listavacia = False

    # Si ya no hay más fotos disponibles de un avistamiento, o llegué al final
    if (((not hayfotos) and (not listavacia))
            or (i == form.list[len(form.list) - 1])):
        # Guardo la lista temporal de fotos a la lista de fotos
        fotos.append(listatemporal)
        listatemporal = []
        listavacia = True

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = []
if not isinstance(form["tipo-avistamiento"], list):  # Si no hay una lista de elementos de tipo
    # Entonces nos informan un solo avistamiento

    if 'sector' not in form:
        sector = ""
    else:
        sector = form['sector'].value
    if 'celular' not in form:
        celular = ""
    else:
        celular = form['celular'].value

    datos = (
        now, form['region'].value, form['comuna'].value, sector,
        form['nombre'].value, form['email'].value, celular,
        form['dia-hora-avistamiento'], form['tipo-avistamiento'],
        form['estado-avistamiento'], fotos
    )
    data.append(datos)
else:
    # Si no, me entregaron más elementos
    datosbase = (
        now, form['region'].value, form['comuna'].value, form['sector'].value,
        form['nombre'].value, form['email'].value, form['celular']
    )
    data.append(datosbase)

    for i in range(0, len(form["tipo-avistamiento"])):
        datoslista = (
            form['dia-hora-avistamiento'][i], form['tipo-avistamiento'][i],
            form['estado-avistamiento'][i], fotos[i]
        )
        data.append(datoslista)

html1 = """
<!DOCTYPE html>
<html lang="en">
    <meta charset="UTF-8">
    <title> RegistroBichos - Informar </title>
    <link rel="shortcut icon" href="img/emoji.ico" />
    <style>
        /* Body of the page*/
        body {
            font-family: Helvetica, sans-serif;
            margin: 0;
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
            text-align: left;
            border: 1px solid black;
        }
    </style>
    </head>

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
        
        <a href="avistamientos.py?pag={0}" >
            <button class="button" > Registro de Avistamientos </button>
        </a>
        <a href="../stats.html">
            <button class="button"> Estadísticas </button>
        </a>
    <p>
</div>

<div class="jump"></div>

<div class="subsubtitle"> Avistamiento Informado Exitosamente </div>

<div class="jump"></div>

</body>

</html>
"""

html2 = """
<!DOCTYPE html>
<html lang="en">
    <meta charset="UTF-8">
    <title> RegistroBichos - Informar </title>
    <link rel="shortcut icon" href="img/emoji.ico" />
    <style>
        /* Body of the page*/
        body {
            font-family: Helvetica, sans-serif;
            margin: 0;
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
            text-align: left;
            border: 1px solid black;
        }
    </style>
    </head>

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
        
        <a href="avistamientos.py?pag={0}" >
            <button class="button" > Registro de Avistamientos </button>
        </a>
        <a href="../stats.html">
            <button class="button"> Estadísticas </button>
        </a>
    <p>
</div>

<div class="jump"></div>

<div class="subsubtitle"> Lo sentimos, ha habido un error </div>

<div class="jump"></div>

</body>

</html>
"""

if database.save_avistamiento(data) == 1:
    print(html1, file=utf8stdout)
else:
    print(html2, file=utf8stdout)
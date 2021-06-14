#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()

import db
from datetime import datetime
import re as regex
import os

print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
database = db.Avistamiento("localhost", "cc500258_u", "uereturpis", "cc500258_db")

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
if not isinstance(form["dia-hora-avistamiento"], list):  # Si no hay una lista de elementos de tipo
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

    if 'sector' not in form:
        sector = ""
    else:
        sector = form['sector'].value
    if 'celular' not in form:
        celular = ""
    else:
        celular = form['celular'].value

    datosbase = (
        now, form['region'].value, form['comuna'].value, sector,
        form['nombre'].value, form['email'].value, celular
    )
    data.append(datosbase)

    for i in range(0, len(form["dia-hora-avistamiento"])):
        datoslista = (
            form['dia-hora-avistamiento'][i], form['tipo-avistamiento'][i],
            form['estado-avistamiento'][i], fotos[i]
        )
        data.append(datoslista)

def verificador(data):
    nombreRegex = "^[a-zA-Z ]*$"
    celularRegex = "([9])+[0-9]{8}$"
    mailRegex = "^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$"

    region = data[0][1]
    comuna = data[0][2]
    sector = data[0][3]
    nombre = data[0][4]
    mail = data[0][5]
    celular = data[0][6]

    if type(region) != str or region == "":
        return "La región ingresada no es válida"

    if type(comuna) != str or comuna == "":
        return "La comuna ingresada no es válida"

    if type(nombre) != str or nombre == "" or not regex.search(nombreRegex, nombre) or len(nombre) > 200:
        return "El nombre ingresado no es válido"

    if type(mail) != str or mail == "" or not regex.search(mailRegex, mail):
        return "El E-Mail ingresado no es válido"

    if type(sector) != str:
        return "El sector ingresado no es válido"

    if type(celular) != str or (len(celular) != 0 and (not regex.search(celularRegex, celular) or len(celular) != 9)):
        return "El celular ingresado no es válido"


    hora_diaRegex = "^[0-9]{4}[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01]) (2[0-3]|[0-1][0-9]):([0-5][0-9])*$"

    # Si es solo un avistamiento, entonces verifico las horas y fotos de uno
    # Recordar que si es solo un avist, todo viene en el primer elemento de data
    if len(data[0]) > 7:
        hora = data[0][7].value
        tipo = data[0][8].value
        estado = data[0][9].value
        fotos = data[0][10]

        if not regex.search(hora_diaRegex, hora):
            return "La hora ingresada no es válida"

        if tipo == "":
            return "El tipo ingresado no es válido"

        if estado == "":
            return "El estado ingresado no es válido"

        path = []
        max_file_size = 10000 * 1000
        for foto in fotos:
            filename = foto.filename
            if not filename:
                return "No se ha subido un archivo"
            size = os.fstat(foto.file.fileno()).st_size

            if size > max_file_size:
                return "El tamaño del archivo excede los 10mb"

            total = cantBase + 1
            cantBase = cantBase + 1
            hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]
            file_path = '../media/' + hash_archivo
            open(file_path, 'wb').write(foto.file.read())
            tipo = filetype.guess(file_path)

            path.append(hash_archivo)

            if (tipo.mime != 'image/jpg') and (tipo.mime != 'image/png') and (tipo.mime != 'image/jpeg'):
                paths.append(path)
                remove(paths)
                return "la foto ingresada no es jpg,png ni jpeg <br>"

    # Si son varios avistamientos, debo recorrer cada avistamiento de la lista
    else:

    hora_dias = form['dia-hora-avistamiento'] if isinstance(form['dia-hora-avistamiento'], list) else [
        form['dia-hora-avistamiento']]
    tipos = form['tipo-avistamiento'] if isinstance(form['tipo-avistamiento'], list) else [form['tipo-avistamiento']]
    estados = form['estado-avistamiento'] if isinstance(form['estado-avistamiento'], list) else [
        form['estado-avistamiento']]
    fotos = listOfFoto(form)
    MAX_FILE_SIZE = 10000 * 1000
    paths = []


        '''Datos del avistamiento'''
        cantBase = database.cantidadFotos()
        for i in range(cantidad):
            if not regex.search(hora_diaRegex, hora_dias[i].value):
                return  "la hora ingresada no es valida <br>"

            if tipos[i].value not in ["A", "M", "I","N"]:
                return "el tipo ingresado no es valida <br>"

            if estados[i].value not in ["M", "V", "N"]:
                return "el sector ingresado no es valido <br>"

            archivos = fotos[i]
            path=[]
            for foto in archivos:

                filename = foto.filename
                if not filename:
                    return "no se subio archivo <br>"
                size = os.fstat(foto.file.fileno()).st_size

                if size > MAX_FILE_SIZE:
                    return "el tamaño excede los 10mb <br>"

                total = cantBase + 1
                cantBase=cantBase+1
                hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]
                file_path = '../media/' + hash_archivo
                open(file_path, 'wb').write(foto.file.read())
                tipo = filetype.guess(file_path)

                path.append(hash_archivo)

                if (tipo.mime != 'image/jpg') and (tipo.mime != 'image/png') and (tipo.mime != 'image/jpeg'):
                    paths.append(path)
                    remove(paths)
                    return "la foto ingresada no es jpg,png ni jpeg <br>"
            paths.append(path)

        else:

            dataObligatoria = (
                form['region'].value, form['comuna'].value,
                form['nombre'].value,
                form['email'].value,
                form['dia-hora-avistamiento'], form['tipo-avistamiento'],
                form['estado-avistamiento'], listOfFoto(form),
                paths
            )
            dataOpcional = (form['sector'].value, form['celular'].value)
            data = (dataObligatoria, dataOpcional)

            database.save_avistamiento(data)
            return "ok"

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
        
        <a href="avistamientos.py?pag=1" >
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

<div class="leyenda">
    <a href="Portada.py">
        <button class="button"> Volver a Portada </button>
    </a>
</div>

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
        
        <a href="avistamientos.py?pag=1" >
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

<div class="leyenda">
    <a href="Portada.py">
        <button class="button"> Volver a Portada </button>
    </a>
</div>

</body>

</html>
"""

if database.save_avistamiento(data) == 1:
    print(html1, file=utf8stdout)
else:
    print(html2, file=utf8stdout)
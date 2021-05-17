#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
import db

database = db.Avistamiento("localhost", "root", "", "tarea2")
data = database.get_last_five_avistamientos()

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
        <form method="post" action="informar.html" style="display:inline">
            <button class="button"> Informar avistamiento </button>
        </form>
        <form method="post" action="Listado.py?pag={0}" style="display:inline">
            <button class="button" > Registro de Avistamientos </button>
        </form>
        <form method="post" action="stats.html" style="display:inline">
            <button class="button"> Estadísticas </button>
        </form>
    <p>
</div>

<div class="jump"></div>

<div class="subsubtitle"> Últimos avistamientos </div>
'''

body2 = '''
<div class="info">
    <div class="leyenda">
        <!-- We start a table to organize the info menu -->
        <table class="table">
            <!-- First row -->
            <tr>
                <th scope="col"> Fecha/Hora </th>
                <th scope="col"> Comuna </th>
                <th scope="col"> Sector </th>
                <th scope="col"> Tipo </th>
                <th scope="col"> Foto </th>
            </tr>
'''

print(head)
print(body1)
print(body2)

if len(data) == 0:
    row = f'''
        <tr>
        <th colspan="5"> Sin datos> </th>
        </tr>
        '''
    print(row)

else:
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

foot = '''
</table>
        <!-- We close the table -->
    </div>
</div>

<div class="jump"></div>

</body>

</html>
'''

print(foot)
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

body = '''
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
        <form method="post" action="avistamientos.html" style="display:inline">
            <button class="button" > Registro de Avistamientos </button>
        </form>
        <form method="post" action="stats.html" style="display:inline">
            <button class="button"> Estadísticas </button>
        </form>
    <p>
</div>

<div class="jump"></div>

<div class="subsubtitle"> Últimos avistamientos </div>

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

            <!-- Second row -->
            <tr>
                <td> 2021-04-14 16:22 </td>
                <td> Peñalolén </td>
                <td> Lo Hermida </td>
                <td> Insecto </td>
                <td> <img src="img/polilla.jpg" alt="" width="200"> </td>
            </tr>

            <!-- Third row -->
            <tr>
                <td> 2021-04-13 12:45 </td>
                <td> Ñuñoa </td>
                <td> Rosita Renard </td>
                <td> Arácnido </td>
                <td> <img src="img/tigre.jpg" alt="" width="200"> </td>
            </tr>

            <!-- Fourth row -->
            <tr>
                <td> 2021-04-11 12:37 </td>
                <td> Peñalolén </td>
                <td> Alto Peñalolén </td>
                <td> Arácnido </td>
                <td> <img src="img/tarantula.jpg" alt="" width="200"> </td>
            </tr>

            <!-- Fifth row -->
            <tr>
                <td> 2021-04-09 19:56 </td>
                <td> Angol </td>
                <td> Villa vieja </td>
                <td> Miriápodo </td>
                <td> <img src="img/cienpies.jpg" alt="" width="200"> </td>
            </tr>

            <!-- Sixth row -->
            <tr>
                <td> 2021-04-03 10:17 </td>
                <td> Valparaiso </td>
                <td> Villa Alemana </td>
                <td> Insecto </td>
                <td> <img src="img/chinita.jpg" alt="" width="200"> </td>
            </tr>
        </table>
        <!-- We close the table -->
    </div>
</div>

<div class="jump"></div>

</body>

</html>
'''
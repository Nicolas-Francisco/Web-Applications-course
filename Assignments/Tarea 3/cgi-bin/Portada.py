#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
import db

print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
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

    <p class="leyenda" >
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

print(head, file=utf8stdout)
print(body1, file=utf8stdout)
print(body2, file=utf8stdout)

if len(data[0]) == 0:
    row = f'''
        <tr>
        <th colspan="5"> Sin datos </th>
        </tr>
        '''
    print(row, file=utf8stdout)

else:
    for i in range(len(data[0])):

        if data[0][i][2] is None:
            sector = "No informado"
        else:
            sector = data[0][i][2]

        row = f'''
        <tr>
        <th> {str(data[0][i][0])} </th>
        <th> {str(data[0][i][1])} </th>
        <th> {str(sector)} </th>
        <th> {str(data[0][i][3])} </th>
        <th> <img class="size" src=../media/{str(data[1][i])} width="120px" height="120px"> </th>
        </tr>
        '''
        print(row, file=utf8stdout)

foot = '''
</table>
        <!-- We close the table -->
    </div>
</div>

<div class="jump"></div>

<div class="subsubtitle"> Mapa de Avistamientos </div>

<div class="jump"></div>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" 
integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" 
crossorigin=""></script>

<div id="mapid" style="width: 600px; height: 400px;"></div>

<script>
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'macadores.py', true);
    xhr.send()
    xhr.timeout = 5000;
    xhr.onload = function (data){
        let coordenadas_comunas = JSON.parse(data.currentTarget.responseText);
        let comunas = Objet.keys(coordenadas_comunas);
        let coordenadas = Object.values(coordenadas_comunas);
        
        var mymap = L.map('mapid').setView([-33.4500000,-70.6666667], 13);
        
        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', 
        {maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1}).addTo(mymap);
        
        for (let i=0; i<comunas.length; i++){
            let comuna = comunas[i];
            let lat = parseFloat(coordenadas_comunas[comuna][0]);
            let lng = parseFloat(coordenadas_comunas[comuna][1]);
            
            let marker = L.marker([lat, lng], {title:"Cantidad de avistamientos en la comuna de "+comuna+": "
            +coordenadas_comunas[comuna][2]}).addTo(mymap);
            
            marker.on('click', function(marker_comuna){
            
            })
        }
    }
    var popup = L.popup();

    function onMapClick(e) {popup.setLatLng(e.latlng).setContent("You clicked the map at " + e.latlng.toString())
    .openOn(mymap);}
    
    mymap.on('click', onMapClick);
</script>

</body>

</html>
'''

print(foot, file=utf8stdout)
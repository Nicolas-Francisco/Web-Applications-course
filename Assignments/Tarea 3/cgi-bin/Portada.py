#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
import db

print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
database = db.Avistamiento("localhost", "cc500258_u", "uereturpis", "cc500258_db")
data = database.get_last_five_avistamientos()

head = '''
<!DOCTYPE html>
<html lang="en">
    <meta charset="UTF-8">
    <title> RegistroBichos </title>
    <link rel="shortcut icon" href="../img/emoji.ico" />
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
        <th> <img class="size" src=../media/{str(data[1][i])} width="120" height="120" alt="img"> </th>
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

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>


<div id="mapid" style="margin:auto; width: 600px; height: 400px;"></div>

<div class="jump"></div>

<script>
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'marcadores.py', true);
    xhr.send()
    xhr.timeout = 5000;
    xhr.onload = function (data){
        let coordenadas_comunas = JSON.parse(data.currentTarget.responseText);
        let comunas = Object.keys(coordenadas_comunas);
        let coordenadas = Object.values(coordenadas_comunas);
        
        var mymap = L.map('mapid').setView([-33.4500000,-70.6666667], 11);
        
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
            
            let marker = L.marker([lat, lng], {title:"Cantidad de avistamientos en la comuna de "+comuna+": "+
            coordenadas_comunas[comuna][2]}).addTo(mymap);
            
            marker.on('click', on_click)
            
            function on_click(marker_comuna){
                let lat = marker_comuna.latlng["lat"]
                let lng = marker_comuna.latlng["lng"]
                let name_comuna;
                
                for (let j=0; j<coordenadas.length; j++){
                    let array = coordenadas[j];
                    let lat_str = array[0];
                    let lng_str = array[1];
                    let lat_float = parseFloat(lat_str);
                    let lng_float = parseFloat(lng_str);
                    
                    if (lat == lat_float && lng == lng_float){
                        name_comuna = comunas[j];
                        break;
                    }
                }
         
                let xhr_map = new XMLHttpRequest();
                let data = new FormData();
                data.append('comuna', name_comuna);
                xhr_map.open('POST', 'map_marker.py');
                xhr_map.send(data);
                xhr_map.timeout = 5000;
                xhr_map.onload = function(data) {
                    let listado = JSON.parse(data.currentTarget.responseText);
                    let llaves = Object.keys(listado);
                    let datos = Object.values(listado);
                    
                    html = `<table>
                        <caption> Avistamientos de la comuna </caption>
                        <tr>
                            <th> Fecha-Hora </th>
                            <th> Tipo </th>
                            <th> Estado </th>
                            <th> Foto </th>
                            <th> Enlace </th>
                        </tr> `;
                        
                    for (let i = 0; i<llaves.length; i++){
                        let llave = llaves[i];
                        let hora = listado[llave][0];
                        let tipo = listado[llave][1];
                        let estado = listado[llave][2];
                        let path = listado[llave][3];
                        let id = listado[llave][4];
                        
                        html+= `<tr> 
                            <td>${hora}</td>
                            <td>${tipo}</td>
                            <td>${estado}</td>
                            <td><img src=../media/${path} width="40" height="40"></td>
                            <td><a href="Informacion.py?id=${id}&pag=1"> Ver avistamiento </td>
                        </tr>`;
                    }
                    html += `</table>`;
                    
                    marker.bindPopup(html);
                }
            }
        }
    };
</script>

</body>

</html>
'''

print(foot, file=utf8stdout)
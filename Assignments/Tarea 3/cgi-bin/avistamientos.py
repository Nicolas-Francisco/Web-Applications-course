#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb;

cgitb.enable()
import db

pag = cgi.FieldStorage().getfirst("pag")
if pag is None:
    pag = 1

print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
database = db.Avistamiento("localhost", "cc500258_u", "uereturpis", "cc500258_db")
data = database.get_avistamientos(int(pag)-1)

head = '''
<!DOCTYPE html>
<html lang="en">
    <meta charset="UTF-8">
    <title> RegistroBichos - Avistamientos </title>
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

<div class="subsubtitle"> Listado de Avistamientos </div>
'''

body2 = '''
<div class="info">
    <div class="leyenda">
        <!-- We start a table to organize the info menu -->
        <table class="table" id="tabla">
            <!-- First row -->
            <tr>
                <th scope="col"> Fecha/Hora </th>
                <th scope="col"> Comuna </th>
                <th scope="col"> Sector </th>
                <th scope="col"> Nombre Contacto </th>
                <th scope="col"> Total Avistamientos </th>
                <th scope="col"> Total Fotos </th>
            </tr>
'''

print(head, file=utf8stdout)
print(body1, file=utf8stdout)
print(body2, file=utf8stdout)

if len(data[0]) == 0:
    row = f'''
        <tr>
        <th colspan="6"> Sin datos </th>
        </tr>
        '''
    print(row, file=utf8stdout)

else:
    for i in range(len(data[0])):

        if data[0][i][3] is None:
            sector = "No informado"
        else:
            sector = data[0][i][3]

        row = f'''
        <tr onclick="show_info({int(data[0][i][0])}, {int(pag)})">
        <th>{str(data[0][i][2])}</th>
        <th>{str(data[2][i])}</th>
        <th>{str(sector)}</th>
        <th>{str(data[0][i][4])}</th>
        <th>{str(data[1][i])}</th>
        <th>{str(data[4][i])} </th>
        </tr>
        '''
        print(row, file=utf8stdout)

foot = '''
</table>
        <!-- We close the table -->
    </div>
</div>

<div class="jump"></div>

<div class="leyenda">
    <button class="button" id="anterior" onclick="to_back()"> Anterior </button>
    
    <button class="button" id="siguiente" onclick="to_next()"> Siguiente </button>
</div>

</body>

<script>
    document.body.onload = show_buttons;
    
    function page(){
        let rutaAbsoluta = self.location.href;
        let posicionNumero = rutaAbsoluta.lastIndexOf("=");
        let rutaRelativa = rutaAbsoluta.substring(posicionNumero + "=".length , rutaAbsoluta.length);
        return rutaRelativa;
    }

    function show_buttons(){
        let pag = parseInt(page());
        
        // Si estoy en la primera página, entonces no hay botón atrás
        if (pag == 1){
            let boton_atras = document.getElementById("anterior");
            boton_atras.setAttribute('style', 'display: none');
        }
        
        // Si la tabla no está llena, entonces no hay botón adelante
        let filas_tabla = document.getElementById("tabla").rows.length;
        if (filas_tabla < 6){
            let boton_next = document.getElementById("siguiente");
            boton_next.setAttribute('style', 'display: none');
        }
    }   
        
    function to_back(){
        let newpag = parseInt(page()) - 1;
        if (!(newpag == 0)){
            let ref = "avistamientos.py?pag=" + newpag.toString();
            location.href = ref;
        }
    }
    
    function to_next(){
        let newpag = parseInt(page()) + 1;
        let ref = "avistamientos.py?pag=" + newpag.toString();
        location.href = ref;
    }
    
    function show_info(id_avist, pag){
        let ref = "Informacion.py?pag=" + pag.toString() + "&id=" + id_avist.toString();
        location.href = ref;
    }
    
</script>

</html>
'''

print(foot, file=utf8stdout)
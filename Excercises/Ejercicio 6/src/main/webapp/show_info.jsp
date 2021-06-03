<%--
  Created by IntelliJ IDEA.
  User: Nico
  Date: 03-06-2021
  Time: 0:26
  To change this template use File | Settings | File Templates.
--%>
<%@ page import="com.cc5002.ejercicio6.Doctor" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<link rel="stylesheet" type="text/css" media="screen"  href="css/index.css" />
<meta charset="UTF-8">
<title>Ejercicio6</title>

</head>

<body>

<ul class="topnav">
    <li><a class="active" href="index.html">Inicio</a></li>
    <li><a href="add_new_doctor.html">Agregar Datos de Médico</a></li>
    <li><a href="list.html">Ver Médicos</a></li>
</ul>

<div>

    <% Doctor doctor = (Doctor) request.getAttribute("doctor"); %>

    <h1>Ficha del médico: <% out.println(doctor.getNombre()); %>  </h1>
    <br>
    <table>
        <!-- intro row -->
        <tr>
            <th>Campo de información</th>
            <th>Información del Médico</th>
        </tr>

        <!-- Región médico -->
        <tr>
            <th>Región del Médico</th>
            <th> <% out.println(doctor.getRegion()); %> </th>
        </tr>

        <!-- Comuna row  -->
        <tr>
            <th>Comuna del Médico</th>
            <th> <% out.println(doctor.getComuna()); %> </th>
        </tr>

        <!-- Nombre row -->
        <tr>
            <th>Nombre del médico</th>
            <th> <% out.println(doctor.getNombre()); %> </th>
        </tr>

        <!-- Experiencia row -->
        <tr>
            <th>Experiencia</th>
            <th> <% out.println(doctor.getExp()); %> </th>
        </tr>

        <!-- Especialidad row -->
        <tr>
            <th>Especialidades</th>
            <th> <% out.println(doctor.getEspecialidad()); %> </th>
        </tr>

        <!-- Twitter row -->
        <tr>
            <th>Twitter del médico</th>
            <th> <% out.println(doctor.getTwitter()); %> </th>
        </tr>

        <!-- Email row -->
        <tr>
            <th>Email del médico</th>
            <th> <% out.println(doctor.getEmail()); %> </th>
        </tr>

        <!-- Número row -->
        <tr>
            <th>Número de celular del médico</th>
            <th> <% out.println(doctor.getCelular()); %> </th>
        </tr>
    </table>

</div>

</body>

</html>

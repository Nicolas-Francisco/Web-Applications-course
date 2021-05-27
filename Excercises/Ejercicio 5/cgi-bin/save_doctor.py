#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import os
import filetype

cgitb.enable()
from db import Doctor

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()

doctordb = Doctor("localhost", "root", "", "ejercicio5")  # #database del doctor


data = (
    form['nombre-medico'].value, form['experiencia-medico'].value, form['especialidad-medico'].value, form['email-medico'].value,
    form['celular-medico'].value, form['file'])

doctordb.save_doctor(data)


#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb;

cgitb.enable()
import db

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)



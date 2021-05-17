#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import hashlib
import os
import filetype

regiones = {}

class Avistamiento
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.db.cursor()

    def get_last_five_avistamientos(self):
        sql = ''' 
        SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo 
        FROM avistamiento AV, detalle_avistamiento DA, comuna CO 
        WHERE DA.avistamiento_id = AV.id 
        AND AV.comuna_id=CO.id 
        ORDER BY DA.dia_hora 
        DESC LIMIT 5 
        '''
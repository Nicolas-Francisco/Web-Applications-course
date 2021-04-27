#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

db = mysql.connector.connect(
  host="localhost",       # 127.0.0.1cd cgi
  user="root",
  password="",
  database="ejercicio3"
)

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS `ejercicio3`.`medico` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(20) NOT NULL,
  `experiencia` VARCHAR (1000) NOT NULL,
  `especialidad` VARCHAR(20) NOT NULL,
  `foto` VARCHAR (1000) NOT NULL,
  `email` VARCHAR(100) NULL,
  `celular` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;
''')

print("La tabla se creo con éxito!")
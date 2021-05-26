#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

db = mysql.connector.connect(
  host="localhost",       # 127.0.0.1cd cgi
  user="root",
  password="",
  database="ejercicio4"
)

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS `ejercicio4`.`archivo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(256) NOT NULL,
  `path` VARCHAR (256) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS `ejercicio4`.`medico` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(20) NOT NULL,
  `experiencia` VARCHAR (1000) NOT NULL,
  `especialidad` VARCHAR(20) NOT NULL,
  `foto` INT NOT NULL,
  `email` VARCHAR(100) NULL,
  `celular` VARCHAR(100) NULL,
  FOREIGN KEY (foto) REFERENCES archivo(id),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;
''')

print("La tabla se creo con éxito!")
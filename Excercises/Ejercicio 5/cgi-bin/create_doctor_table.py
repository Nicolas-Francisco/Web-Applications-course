#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ejercicio5"
)

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS `ejercicio5`.`archivo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(256) NOT NULL,
  `path` VARCHAR (256) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS `ejercicio5`.`medico` (
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
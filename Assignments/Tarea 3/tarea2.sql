-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema cc500258_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cc500258_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cc500258_db` DEFAULT CHARACTER SET utf8 ;
USE `cc500258_db` ;

-- -----------------------------------------------------
-- Table `cc500258_db`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500258_db`.`region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cc500258_db`.`comuna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500258_db`.`comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `cc500258_db`.`region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_comuna_region1_idx` ON `cc500258_db`.`comuna` (`region_id` ASC);


-- -----------------------------------------------------
-- Table `cc500258_db`.`avistamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500258_db`.`avistamiento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `dia_hora` DATETIME NOT NULL,
  `sector` VARCHAR(200) NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `celular` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_domicilio_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `cc500258_db`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_domicilio_comuna1_idx` ON `cc500258_db`.`avistamiento` (`comuna_id` ASC);


-- -----------------------------------------------------
-- Table `cc500258_db`.`detalle_avistamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500258_db`.`detalle_avistamiento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `dia_hora` DATETIME NOT NULL,
  `tipo` ENUM('no sé', 'insecto', 'arácnido', 'miriápodo') NOT NULL,
  `estado` ENUM('no sé', 'vivo', 'muerto') NOT NULL,
  `avistamiento_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_detalle_avistamiento_avistamiento1`
    FOREIGN KEY (`avistamiento_id`)
    REFERENCES `cc500258_db`.`avistamiento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_detalle_avistamiento_avistamiento1_idx` ON `cc500258_db`.`detalle_avistamiento` (`avistamiento_id` ASC);


-- -----------------------------------------------------
-- Table `cc500258_db`.`foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cc500258_db`.`foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ruta_archivo` VARCHAR(300) NOT NULL,
  `nombre_archivo` VARCHAR(300) NOT NULL,
  `detalle_avistamiento_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_foto_detalle_avistamiento1`
    FOREIGN KEY (`detalle_avistamiento_id`)
    REFERENCES `cc500258_db`.`detalle_avistamiento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_foto_detalle_avistamiento1_idx` ON `cc500258_db`.`foto` (`detalle_avistamiento_id` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

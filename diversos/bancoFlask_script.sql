create database bancoFlask;
use bancoFlask;

create table person(
codigo INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(150) NOT NULL,
telefone VARCHAR(150) NOT NULL,
endereco VARCHAR(200) NOT NULL,
data_nascimento DATE NOT NULL
)Engine=InnoDB;

DROP TABLE person;

SELECT * FROM person;
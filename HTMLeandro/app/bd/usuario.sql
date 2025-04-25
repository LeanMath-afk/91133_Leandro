CREATE DATABASE IF NOT EXISTS estoque;

USE estoque;

CREATE table IF not EXISTS usuarios(
    id int AUTO_INCREMENT PRIMARY KEY,
    usuario varchar(50) not null unique,
    senha varchar(255) not null
);

insert into usuarios (usuario,senha)
values ('admin',password ('admin123'));
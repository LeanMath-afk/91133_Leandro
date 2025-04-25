CREATE DATABASE estoque;

USE estoque;

CREATE table produtos(
    id int AUTO_INCREMENT PRIMARY KEY,
    produto varchar(100) not null,
    tipo varchar(50) not null,
    quantidade int not null
);
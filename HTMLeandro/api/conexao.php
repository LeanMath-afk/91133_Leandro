<?php

if($_SERVER['REQUEST_METHOD'] !== 'POST'){
    header("location: http://localhost/api/index.html");
    exit
}

$host = "localhost";
$usuario = "root";
$senha = "";
$banco = "estoque";

$conn = new mysqli($host,$usuario,$senha,$banco);

if ($conn->connection_error){
    die("conexão falhou: " . $conn->connection_error);
}
echo("conectado!");
?>
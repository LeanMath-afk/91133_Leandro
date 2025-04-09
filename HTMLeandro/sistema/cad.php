<?php

$host = "localhost";
$user = "root";
$pass = "";
$dbname = "cadastro_produtos";

$conn = new mysqli($host,$user,$pass,$dbname);

if ($conn->connection_error){
    die("conexão falhou: " . $conn->connection_error);
}
echo("conectado!");
?>
<?php 

if($_SERVER['REQUEST_METHOD'] !== 'POST'){
    header("location: http://localhost/api/index.html");
    exit
}

include 'autenticar.php';
include 'conexao.php';
include 'insere.php';
include '/view/conecta.php';

echo "<script>
    alert('cadastro realizado com sucesso!');
    window.location.href = 'http://localhost/api/index.html';
</script>";
?>    
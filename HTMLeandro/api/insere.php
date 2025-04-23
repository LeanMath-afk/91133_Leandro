<?php

if($_SERVER['REQUEST_METHOD'] !== 'POST'){
    header("location: http://localhost/api/index.html");
    exit
}

if(empty($usuario) || empty($senha)) {
    echo "<script>
    alert ('preencha todos os campos.');
    window.location.href = 'index.html';
    </script>";
    exit;
}

$stmt = $conn->prepare("SELECT * FROM usuarios WHERE usuarios = ? and senha = password(?)");
$stmt->bind_param("ss",$usuario,$senha);
$stmt->execute();
$resultado = $stmt->get_result();

if($resultado->num_rows === 1){
    $_SESSION['usuario'] = $usuario;
    echo "<script>
    alert ('login feito com sucesso!.');
    window.location.href = 'http://localhost/api/cad.html';
    </script>";
    exit;
} else {
    echo "<script>
    alert ('login ou senha incorrentos!');
    window.location.href = 'http://localhost/api/cad.html';
    </script>";
    exit;
}

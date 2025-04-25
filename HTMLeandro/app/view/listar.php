<?php
include 'conecta.php';
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilo.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"&gt;>
    <title>Controle de Estoque 1.0</title>
</head>
<body>
    <?php
    $sql = "SELECT * FROM produtos ORDER BY id DESC";
    $resultado = $conn->query($sql);

    if($resultado->num_rows > 0){
        echo"<table>";
        echo"<thead>
                <tr>
                    <th>ID</th>
                    <th>Produto</th>
                    <th>Tipo</th>
                    <th>Quantidade</th>
                    <th>Ações</th>
                </tr>
            </thead>";
        echo "<tbody>":
        while($linha = $resultado->fetch_assoc()){
            echo "<tr>";
            echo "<td>".$linha['id']."</td>";
            echo "<td>".htmlspecialchars($linha['produto'])."</td>";
            echo "<td>".htmlspecialchars($linha['tipo'])."</td>";
            echo "<td>".htmlspecialchars($linha['quantidade'])."</td>";
            echo "<td>
                
                    <a href='api/api.php?acao=editar&id=".$linha['id'] . "' 
                    tittle='Editar'>
                        <i class="'fas fa-edit' style='color:blue;'></i>
                    </a>
                      

                    <a href='excluir.php?id=" . $linha['id'] ."' 
                    tittle='Excluir' onclick=\"return confirm(''Você tem certeza que deseja excluir este produto?')\">
                        <i class='fa-solid fa-trash' style='color:red;'></i>
                    </a>
                  </td>";
            echo "</tr>";
            echo "<tbody>";
            echo "</table>";
        }else{
            echo "<p>Nenhum produto encontrado.</p>";
        }
    }
    ?>
    
</body>
</html>
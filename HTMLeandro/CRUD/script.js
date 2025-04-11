function validar(){
    const nome = document.getElementById("nome").value.trim();
    const tel = document.getElementById("telefone").value.trim();
    const email = document.getElementById("email").value.trim();

    if (!nome || !tel || !email){
        alert("Preencha todos os campos!");
        return false;
    }
    return true;
} 
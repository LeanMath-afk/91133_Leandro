document.getElementById("loginForm").addEventListener("submit", function(event){
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password){
        alert("Por favor,preencha todos os campos");
        return;
    }

    if (password.length < 8){
        alert("a senha deve conter 8 dígitos");
        return;
    }

    localStorage.setItem("username",username);
    window.location.href = "painel.html";
    alert("Login efetuado com sucesso!");
});
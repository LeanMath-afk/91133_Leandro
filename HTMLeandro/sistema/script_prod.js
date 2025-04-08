const produtos = {
    produto1: 10.00,
    produto2: 20.00,
    produto3: 30.00,
    produto4: 40.00
};

document.getElementById("produto").addEventListener("change", function() {
    const produtoSelecionado = this.value;
    const preco = produtos[produtoSelecionado];
    document.getElementById("preco").value = `R$ ${preco.toFixed(2)}`;
    calcularTotal();
});

function calcularTotal() {
    const quantidade = document.getElementById("quantidade").value;
    const produtoSelecionado = document.getElementById("produto").value;
    const preco = produtos[produtoSelecionado];
    const total = preco * quantidade;
    document.getElementById("total").value = `R$ ${total.toFixed(2)}`;
}

document.getElementById("quantidade").addEventListener("input", calcularTotal);

window.onload = function() {
    document.getElementById("produto").dispatchEvent(new Event("change"));
};

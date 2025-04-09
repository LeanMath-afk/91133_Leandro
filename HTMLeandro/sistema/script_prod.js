document.addEventListener('DOMContentLoaded', function () {
    const produtoSelect = document.getElementById('produto');
    const precoInput = document.getElementById('preco');
    const quantidadeInput = document.getElementById('quantidade');
    const totalInput = document.getElementById('total');
    const form = document.getElementById('form-produto');

    const precos = {
        produto1: 10.00,
        produto2: 15.50,
        produto3: 20.75,
        produto4: 12.30
    };

    produtoSelect.addEventListener('change', function () {
        const produtoSelecionado = produtoSelect.value;
        const preco = precos[produtoSelecionado] || 0;
        precoInput.value = preco.toFixed(2);
        atualizarTotal();
    });

    quantidadeInput.addEventListener('input', atualizarTotal);

    function atualizarTotal() {
        const preco = parseFloat(precoInput.value) || 0;
        const quantidade = parseInt(quantidadeInput.value) || 1;
        const total = preco * quantidade;
        totalInput.value = total.toFixed(2);
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const dados = {
            produto: produtoSelect.value,
            preco: precoInput.value,
            quantidade: quantidadeInput.value,
            total: totalInput.value
        };
        console.log('Produto adicionado ao carrinho:', dados);
        alert('Produto adicionado ao carrinho!');
    });

    produtoSelect.dispatchEvent(new Event('change'));
});

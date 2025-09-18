# -------------------------------------------------------
# Arquivo: mercadinho.py
# Autor: Leandro Matheus da Silva de Jesus
# Data: 18/09/2025
# Testes Unitários: CRUD Mercadinho
# -------------------------------------------------------

import unittest
from mercadinho import Mercadinho, Produto  # Certifique-se de que seu código esteja em mercadinho.py

class TestMercadinho(unittest.TestCase):

    # 1. Cadastro de produto válido
    def test_cadastro_produto_valido(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        resultado = mercado.adicionar_produto(produto)
        self.assertTrue(resultado)
        self.assertIn(produto, mercado.listar_produtos())

    # 2. Cadastro de produto duplicado
    def test_cadastro_produto_duplicado(self):
        mercado = Mercadinho()
        produto1 = Produto(1, "Produto1", 10.0, 5)
        produto2 = Produto(1, "ProdutoDuplicado", 15.0, 3)
        mercado.adicionar_produto(produto1)
        resultado = mercado.adicionar_produto(produto2)
        self.assertFalse(resultado)
        self.assertEqual(len(mercado.listar_produtos()), 1)

    # 3. Busca de produto existente
    def test_busca_produto_existente(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto)
        buscado = mercado.buscar_produto(1)
        self.assertIsNotNone(buscado)
        self.assertEqual(buscado.nome, "Produto1")
        self.assertEqual(buscado.preco, 10.0)
        self.assertEqual(buscado.quantidade, 5)

    # 4. Busca de produto inexistente
    def test_busca_produto_inexistente(self):
        mercado = Mercadinho()
        buscado = mercado.buscar_produto(999)
        self.assertIsNone(buscado)

    # 5. Atualização de nome do produto
    def test_atualizacao_nome_produto(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto)
        resultado = mercado.atualizar_produto(1, {"nome": "NovoNome"})
        self.assertTrue(resultado)
        self.assertEqual(produto.nome, "NovoNome")
        self.assertEqual(produto.preco, 10.0)
        self.assertEqual(produto.quantidade, 5)

    # 6. Atualização de preço do produto
    def test_atualizacao_preco_produto(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto)
        resultado = mercado.atualizar_produto(1, {"preco": 20.0})
        self.assertTrue(resultado)
        self.assertEqual(produto.preco, 20.0)

    # 7. Atualização de produto inexistente
    def test_atualizacao_produto_inexistente(self):
        mercado = Mercadinho()
        resultado = mercado.atualizar_produto(999, {"nome": "X"})
        self.assertFalse(resultado)

    # 8. Remoção de produto existente
    def test_remocao_produto_existente(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto)
        resultado = mercado.remover_produto(1)
        self.assertTrue(resultado)
        self.assertNotIn(produto, mercado.listar_produtos())

    # 9. Tentativa de remoção de produto inexistente
    def test_remocao_produto_inexistente(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto)
        resultado = mercado.remover_produto(999)
        self.assertFalse(resultado)
        self.assertIn(produto, mercado.listar_produtos())

    # 10. Listagem de produtos
    def test_listagem_produtos(self):
        mercado = Mercadinho()
        produto1 = Produto(1, "Produto1", 10.0, 5)
        produto2 = Produto(2, "Produto2", 15.0, 3)
        mercado.adicionar_produto(produto1)
        mercado.adicionar_produto(produto2)
        lista = mercado.listar_produtos()
        self.assertEqual(len(lista), 2)
        self.assertIn(produto1, lista)
        self.assertIn(produto2, lista)

    # 11. Limpeza da lista
    def test_limpeza_lista(self):
        mercado = Mercadinho()
        produto1 = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto1)
        mercado.limpar()
        self.assertEqual(len(mercado.listar_produtos()), 0)

    # 12. Controle de estoque
    def test_controle_estoque(self):
        mercado = Mercadinho()
        produto = Produto(1, "Produto1", 10.0, 5)
        mercado.adicionar_produto(produto)
        mercado.atualizar_produto(1, {"quantidade": 10})
        self.assertEqual(produto.quantidade, 10)


if __name__ == "__main__":
    unittest.main()

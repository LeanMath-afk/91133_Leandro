import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    # Testes de soma
    def test_somar_1(self):
        self.assertEqual(calculadora.somar(7, 12), 19)

    def test_somar_2(self):
        self.assertEqual(calculadora.somar(-4, 15), 11)

    def test_somar_3(self):
        self.assertEqual(calculadora.somar(0, 9), 9)

    def test_somar_4(self):
        self.assertEqual(calculadora.somar(-10, -3), -13)

    def test_somar_5(self):
        self.assertAlmostEqual(calculadora.somar(3.5, 2.5), 6.0, places=6)

    # Testes de subtração
    def test_subtrair_1(self):
        self.assertEqual(calculadora.subtrair(20, 8), 12)

    def test_subtrair_2(self):
        self.assertEqual(calculadora.subtrair(-5, -2), -3)

    def test_subtrair_3(self):
        self.assertEqual(calculadora.subtrair(0, 7), -7)

    def test_subtrair_4(self):
        self.assertEqual(calculadora.subtrair(3, -6), 9)

    def test_subtrair_5(self):
        self.assertAlmostEqual(calculadora.subtrair(5.5, 2.2), 3.3, places=6)

    # Testes de multiplicação
    def test_multiplicar_1(self):
        self.assertEqual(calculadora.multiplicar(6, 7), 42)

    def test_multiplicar_2(self):
        self.assertEqual(calculadora.multiplicar(-3, 5), -15)

    def test_multiplicar_3(self):
        self.assertEqual(calculadora.multiplicar(0, 10), 0)

    def test_multiplicar_4(self):
        self.assertEqual(calculadora.multiplicar(-4, -2), 8)

    def test_multiplicar_5(self):
        self.assertAlmostEqual(calculadora.multiplicar(2.5, 4.0), 10.0, places=6)

    # Testes de divisão
    def test_dividir_1(self):
        self.assertEqual(calculadora.dividir(24, 6), 4)

    def test_dividir_2(self):
        self.assertEqual(calculadora.dividir(-15, 3), -5)

    def test_dividir_3(self):
        self.assertEqual(calculadora.dividir(9, 3), 3)

    def test_dividir_4(self):
        self.assertEqual(calculadora.dividir(-8, -4), 2)

    def test_dividir_5(self):
        self.assertAlmostEqual(calculadora.dividir(7.5, 2.5), 3.0, places=6)

    # Teste especial para divisão por zero
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            calculadora.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
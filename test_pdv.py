import unittest

def calcular_total(itens):
    return sum(itens)

class TestSistemaPDV(unittest.TestCase):

    def test_total_inicial(self):
        self.assertEqual(calcular_total([]), 0.0)

    def test_adicionar_hamburguer(self):
        carrinho = [25.0]
        self.assertEqual(calcular_total(carrinho), 25.0)

    def test_adicionar_pizza(self):
        carrinho = [40.0]
        self.assertEqual(calcular_total(carrinho), 40.0)

    def test_soma_combo(self):
        carrinho = [25.0, 8.0] 
        self.assertEqual(calcular_total(carrinho), 33.0)

    def test_valor_positivo(self):
        carrinho = [10.0]
        self.assertGreaterEqual(calcular_total(carrinho), 0)

if __name__ == '__main__':
    unittest.main()
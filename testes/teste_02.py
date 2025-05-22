# Exemplo de Teste Unitário no Google Colab

# 1. Primeiro, vamos criar uma função simples para testar
def soma(a, b):
    """Retorna a soma de dois números"""
    return a + b

def eh_par(num):
    """Verifica se um número é par"""
    return num % 2 == 0

# 2. Agora vamos escrever os testes unitários usando a biblioteca unittest
import unittest

class TestFuncoes(unittest.TestCase):
    
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)
    
    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)
    
    def test_soma_mistos(self):
        self.assertEqual(soma(10, -5), 5)
    
    def test_eh_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(5))
        self.assertTrue(eh_par(0))
    
    def test_soma_tipos_diferentes(self):
        with self.assertRaises(TypeError):
            soma("2", 3)

# 3. Para executar os testes no Colab, precisamos usar um método especial
# em vez de unittest.main()
def run_tests():
    """Função para executar os testes no Google Colab"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFuncoes)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\n🎉 Todos os testes passaram com sucesso!")
    else:
        print("\n❌ Alguns testes falharam.")

# 4. Executar os testes
print("Iniciando os testes unitários...")
run_tests()

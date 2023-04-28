import unittest
import mytest

class TestMiCodigo(unittest.TestCase):
    def test_suma(self):
        resultado = mytest.mi_codigo(2, 3)
        self.assertEqual(resultado, 5)

    def test_suma_err(self):
        resultado = mytest.mi_codigo(2, 7)
        self.assertEqual(resultado, 5)

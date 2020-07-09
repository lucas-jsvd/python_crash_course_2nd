import unittest

from trabalhador import Trabalhador


class TrabalhadorTestCase(unittest.TestCase):
    def setUp(self):
        self.trabalhador = Trabalhador("Lucas", "José", 30_000)

    def test_aumento_padrao(self):
        self.trabalhador.dar_aumento()
        self.assertEqual(self.trabalhador.sal_anual, 35_000)

    def test_aumento_definido(self):
        self.trabalhador.dar_aumento(15000)
        self.assertEqual(self.trabalhador.sal_anual, 45_000)


if __name__ == "__main__":
    unittest.main()

import unittest

from cidade_estado import descricao


class CidadeEstadoTestCase(unittest.TestCase):
    def test_cidade_estado(self):
        teste = descricao("aracaju", "sergipe")
        self.assertEqual(teste, "Aracaju, Sergipe")

    def test_cidade_estado_populacao(self):
        teste = descricao("aracaju", "sergipe", 650_000)
        self.assertEqual(teste, "Aracaju, Sergipe - População 650000")


if __name__ == "__main__":
    unittest.main()

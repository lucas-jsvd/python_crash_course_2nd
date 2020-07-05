from random import randint


class Dado():
    def __init__(self, lados=6):
        self.lados = lados

    def rolar_dado(self):
        lado = randint(1, self.lados)
        print(f'\nLado sorteado: {lado}')


dado_6_lados = Dado()
dado_10_lados = Dado(10)
dado_20_lados = Dado(20)

dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()
dado_6_lados.rolar_dado()

dado_10_lados.rolar_dado()
dado_10_lados.rolar_dado()
dado_10_lados.rolar_dado()
dado_10_lados.rolar_dado()
dado_10_lados.rolar_dado()

dado_20_lados.rolar_dado()
dado_20_lados.rolar_dado()
dado_20_lados.rolar_dado()
dado_20_lados.rolar_dado()
dado_20_lados.rolar_dado()

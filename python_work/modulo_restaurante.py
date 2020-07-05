class Restaurante():
    """Uma classe para descrever restauranes."""

    def __init__(self, nome, cozinha):
        self.nome = nome
        self.cozinha = cozinha
        self.num_atendimento = 0

    def descricao(self):
        print(f'\nNome do restaurante: {self.nome}')
        print(f'Tipo de cozinha: {self.cozinha}')

    def aberto(self):
        print(f'\nO Restaurante, {self.nome}, está aberto.')

    def set_num_atendimento(self, num_atendimento):
        self.num_atendimento = num_atendimento

    def incr_num_atendimento(self, num_atendimento):
        self.num_atendimento += num_atendimento


class CarrinhoSorvete(Restaurante):
    """Classe que representa um carrinho de sorvete."""

    def __init__(self, nome, cozinha):
        super().__init__(nome, cozinha)
        self.sabores = ["Chocolate", "Limão", "Morango", "Kiwi", "Umbu"]

    def exibe_sabores(self):
        print("\nOs sabores disponiveis são: ")
        [print(f'\t{sabor}') for sabor in self.sabores]

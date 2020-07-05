class Usuario():
    """Cria uma classe Usuário."""

    def __init__(self, nome, sobrenome, idade, sexo, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        self.tentativa_login = 0

    def descricao(self):
        msg = f'\nNome: {self.nome}\nSobrenome: {self.sobrenome}'
        msg += f'\nIdade: {self.idade}\nSexo: {self.sexo}'
        msg += f'\nCidade: {self.cidade}'
        print(msg)

    def bem_vindo(self):
        print(f'\nSeja bem-vindo, {self.nome} {self.sobrenome}')

    def incr_tentativa_login(self):
        self.tentativa_login += 1

    def reset_tentativa_login(self):
        self.tentativa_login = 0

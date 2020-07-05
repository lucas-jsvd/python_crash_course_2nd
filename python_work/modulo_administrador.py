from modulo_usuario import Usuario


class Adminitrador(Usuario):
    """Classe que define um usuario administrador."""

    def __init__(self, nome, sobrenome, sexo, idade, cidade):
        super().__init__(nome, sobrenome, sexo, idade, cidade)
        self.privilegios = Privilegios()


class Privilegios():
    """Cria uma classe com os privilégios dos usuarios administradores."""

    def __init__(self):
        self.privilegios = ["Adcionar post", "Deletar post", "Banir Usuario"]

    def exibir_previlegios(self):
        print("\nOs privilegios do administrador são: ")
        [print(f'\t{privilegio}') for privilegio in self.privilegios]

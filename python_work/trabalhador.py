class Trabalhador():
    def __init__(self, nome, sobrenome, sal_anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sal_anual = sal_anual

    def dar_aumento(self, aumento=5000):
        self.sal_anual += aumento

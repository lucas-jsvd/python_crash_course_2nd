nome = "Lucas"
print("O nome Lucas é == \"lucas\". Essa resposta deveria ser falsa.")
print(nome == "lucas")

print("O nome Lucas.lower() = \"lucas\". Essa reposta deveria ser verdadeira.")
print(nome.lower() == "lucas")

idade_lucas = 27
idade_mae = 50
print("A idade de Lucas é igual a idade da sua Mãe ? Essa reposta deveria ser falsa.")
print(idade_lucas == idade_mae)
print("A idade de Lucas é menor que a idade da sua Mãe ? Essa reposta deveria ser verdadeira.")
print(idade_lucas <= idade_mae)
print("A idade de Lucas é maior que 20 anos e a idade de sua mãe é maior que 40 anos ? Essa reposta deveria ser verdadeira.")
print(idade_lucas >= 20 and idade_mae >= 40)

lista_irmaos = ["Henrique", "Dulce", "Ariel", "Claudia"]
print("Henrique é um dos meus irmãos ? Essa resposta deveria ser verdadeira.")
print("Henrique" in lista_irmaos)

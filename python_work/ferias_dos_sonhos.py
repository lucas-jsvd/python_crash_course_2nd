ferias_sonhos = {}

while True:
    nome = input("Qual o seu nome? ")
    local_ferias = input("Qual o local de ferias dos seus sonhos? ")
    ferias_sonhos[nome] = local_ferias

    adcionar = input("Você deseja adcionar mais uma entrada (s/n)? ")

    if adcionar.lower() == "n":
        break

print("As pessoas e locais de ferias adcionados foram: ")
for nome, local_ferias in ferias_sonhos.items():
    print(f'\t {nome} gostaria de passar suas ferias na/o {local_ferias}')

nomes_rios = {"Amazonia": "Brasil", "Nilo": "Egito", "Prata": "Argentina"}
for rio, pais in nomes_rios.items():
    print(f'O rio {rio} fica no país {pais}')
print("Lista de nomes de rios: ")
for rio in nomes_rios:
    print(rio)
print('Lista dos nomes dos paises: ')
for pais in nomes_rios.values():
    print(pais)

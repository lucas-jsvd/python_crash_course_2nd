import json

filename = "num_predileto_comp.txt"


def ler_num_pred():
    try:
        with open(filename) as f:
            conteudo = json.load(f)
    except FileNotFoundError:
        salva_num_pred()
    else:
        print(f"Seu numero predileto é o {conteudo}.")


def salva_num_pred():
    try:
        numero = int(input("Qual o seu numero predileto? "))
    except ValueError:
        print("Você digitou um valor incorreto.")
    else:
        with open(filename, "w") as f:
            json.dump(numero, f)


ler_num_pred()

import json

filename = "num_predileto.txt"
try:
    numero = int(input("Qual o seu numero predileto? "))
except ValueError:
    print("Você digitou um valor incorreto.")
else:
    with open(filename, "w") as f:
        json.dump(numero, f)

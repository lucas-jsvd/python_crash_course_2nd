import json

filename = "num_predileto.txt"
try:
    with open(filename) as f:
        conteudo = json.load(f)
except FileNotFoundError:
    print(f"O arquivo {filename} não existe.")
else:
    print(f"Seu numero predileto é o {conteudo}.")

try:
    arquivo = "livro.txt"
    with open(arquivo, encoding="utf8") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("O arquivo {arquivo} não foi encontrado.")
else:
    print(f'Nesse livro a palavra \"the\" se repete {conteudo.lower().count("the ")} vezes.')

arquivos = ["cachorros.txt", "gatos.txt"]
for arquivo in arquivos:
    try:
        with open(arquivo) as f:
            conteudo = f.read()
    except FileNotFoundError:
        pass
    else:
        print(conteudo)

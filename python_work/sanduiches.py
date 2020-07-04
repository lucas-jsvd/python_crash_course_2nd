def cria_sanduiche(*ingredientes):
    print("O seu sanduiche tera:")
    for ingrediente in ingredientes:
        print(f'\t{ingrediente}')


cria_sanduiche("Carne de Hamburguer", "Mussarela", "Presuto")
cria_sanduiche("Carne de Hamburguer", "Mussarela", "Presuto", "Bacon")
cria_sanduiche("Carne de Hamburguer", "Mussarela", "Presuto", "Ovos")

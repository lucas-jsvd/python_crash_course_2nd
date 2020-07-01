favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

lista_entrevistados = ["jen", "lucas", "simone", "dulce", "edward"]

for entrevistado in lista_entrevistados:
    if entrevistado in favorite_languages.keys():
        print(f"{entrevistado.title()}, obrigado por responder a entrevista.")
    else:
        print(f"{entrevistado.title()}, você ainda não respondeu a entrevista.")

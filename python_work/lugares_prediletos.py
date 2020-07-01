lugares_favoritos = {
    "simone": ["Grecia", "Paris", "Italia"],
    "mario": ["Gana", "Portugual", "Espanha"],
    "lucas": ["China", "Japão", "Vietnam"]
}

for pessoa in lugares_favoritos:
    print(f"\nOs locais prediletos de {pessoa.title()} são: ")
    for lugar in lugares_favoritos[pessoa]:
        print(f'\t{lugar.title()}')

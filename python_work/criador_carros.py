def make_car(marca, modelo, **keys):
    print(f'\nMarca: {marca}')
    print(f'Modelo: {modelo}')
    for key in keys:
        print(f'{key.title()}: {keys[key]}')


make_car("Subaru", "Forester")
make_car("Audi", "A3", color="Prata", ano=2020)
make_car("BMW", "B5", color="Vermelho", ano=2018)

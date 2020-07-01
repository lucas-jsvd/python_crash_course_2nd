lista_pets = []
pet1 = {"tipo": "Cachorro", "dono": "Ariel"}
lista_pets.append(pet1)
pet2 = {"tipo": "Gato", "dono": "Simone"}
lista_pets.append(pet2)
pet3 = {"tipo": "Cagado", "dono": "Rosa"}
lista_pets.append(pet3)

for pet in lista_pets:
    print(f'Nome: {pet["tipo"]},\nSobrenome: {pet["dono"]}\n')

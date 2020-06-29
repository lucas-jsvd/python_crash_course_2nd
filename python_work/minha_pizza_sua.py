lista_pizza = ["margarita", "calabresa", "mussarela", "quatro-queijos", "frango"]
friend_pizza = lista_pizza[:]
lista_pizza.append("nordestina")
friend_pizza.append("bacon")
[print(pizza1, pizza2) for pizza1, pizza2 in zip(lista_pizza, friend_pizza)]
print(lista_pizza)
print(friend_pizza)
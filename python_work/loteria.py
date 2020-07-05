from random import sample


bolas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E")
ticket = (1, 7, "A", 9)
num_loop = 0

while True:
    sorteados = sample(bolas, k=4)
    num_loop += 1
    num_acertos = 0
    for opcao in ticket:
        if opcao in sorteados:
            num_acertos += 1
            print(f"Acertou {num_acertos}")
        else:
            print("Errou")
            break
    if num_acertos == 4:
        break

print("As bolas sorteadas foram: ")
[print(f'\t{sorteado}') for sorteado in sorteados]
print(f"Você foi sorteado depois de {num_loop} loops.")

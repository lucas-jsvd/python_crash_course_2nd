while True:
    try:
        print("Para sair digite 101")
        num_1 = int(input("Digite o primeiro numero: "))
        if num_1 == 101:
            break
        num_2 = int(input("Digite o segundo numero: "))
        if num_2 == 101:
            break
    except ValueError:
        print("Você digitou um tipo de valor incorreto.")
    else:
        print(f'A soma de {num_1} + {num_2} = {num_1 + num_2}')

while True:
    msg = "Qual a idade do comprador do ticket ? "
    msg += "\nPara encerrar o programa digite \"sair\": "
    idade = input(msg)

    if idade.lower() == "sair":
        print("Até a próxima!")
        break

    if int(idade) < 3:
        print(f"Para pessoas com {idade} anos o ticket é grátis.")
    elif int(idade) <= 12:
        print(f"Para pessoas com {idade} anos o ticket custa $10.")
    else:
        print(f"Para pessoas com {idade} anos o ticket custa $15.")

with open("convidados.txt", "w") as file_obj:
    while True:
        nome = input("Qual o seu nome? Se quiser terminar digite \"sair\". ")
        if nome.lower() == "sair":
            break
        file_obj.write(f'{nome}\n')

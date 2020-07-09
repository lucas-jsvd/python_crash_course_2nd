with open("pq_programar.txt", "a") as file_obj:
    while True:
        motivo = input("Pq vc gosta de programar? Se quiser terminar digite \"sair\". ")
        if motivo.lower() == "sair":
            break
        file_obj.write(f'{motivo}\n')

while True:
    msg = "Qual cobertura você deseja adcionar a sua pizza ?"
    msg += "\nDigite \"sair\" para encerar o programa: "
    cobertura = input(msg)

    if cobertura.lower() == "sair":
        print("Até a proxima !")
        break

    print(f'A cobertura de {cobertura} foi adcionada a pizza.')

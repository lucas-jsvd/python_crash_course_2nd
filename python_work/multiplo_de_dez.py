print("Digite um numero e verificarei se ele é um multiplo de dez.")
numero = input("Digite o numero: ")

if int(numero) % 10 == 0:
    print(f'O número {numero} é multiplo de 10.')
else:
    print(f'O número {numero} não é multiplo de 10.')

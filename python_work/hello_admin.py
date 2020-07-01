#lista_usuarios = []
lista_usuarios = ["ariel", "simone", "dulce", "lucas", "admin"]
if lista_usuarios:
    for usuario in lista_usuarios:
        if usuario == "admin":
            print("Olá adminstrador, o que deseja verifiar hoje ?")
        else:
            print(f'Olá {usuario}, obrigado por entrar no sistema.')
else:
    print("Infelizmente não temos nenhum usuário.")

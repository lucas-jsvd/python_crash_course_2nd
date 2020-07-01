usuarios_atuais = ["ariel", "simone", "dulce", "lucas", "admin"]
novos_usuarios = ["ariel", "monica", "claudia", "lucas", "vitoria"]
for usuario in novos_usuarios:
    if usuario.lower() in usuarios_atuais:
        print(f"O nome de usuário, {usuario}, não está disponivel.")
    else:
        print(f'O nome de usuário, {usuario}, está disponivel.')

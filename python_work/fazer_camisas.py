msg_camisa = "Que a força esteja com você."
tamanho_camisa = 36
msg_camisa2 = "A força é forte em você."
tamanho_camisa2 = 42


def make_shirt(text="I love Python", size="large"):
    print('\nFabricaremos uma camisa com as seguintes informações:')
    print(f'\tMensagem: "{text}"')
    print(f'\tTamanho: {size}')


make_shirt(msg_camisa, tamanho_camisa)
make_shirt(size=tamanho_camisa2, text=msg_camisa2)
make_shirt()
make_shirt(size="medium")

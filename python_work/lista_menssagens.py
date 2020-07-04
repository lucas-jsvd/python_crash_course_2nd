mensagens = ["Olá, seja bem-vindo.", "Que a força esteja com você.", "Eu voltarei.", "Tó certo!!!"]
mensagens_enviadas = []

def show_messsages(mensagem):
    print(f'{mensagem}')


def send_messsages(mensagens, mensagens_enviadas):
    while mensagens:
       mensagem = mensagens.pop()
       show_messsages(mensagem)
       mensagens_enviadas.append(mensagem)


send_messsages(mensagens[:], mensagens_enviadas)
print(mensagens, mensagens_enviadas)

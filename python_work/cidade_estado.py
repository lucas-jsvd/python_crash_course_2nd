def descricao(cidade, estado, populacao=None):
    if populacao:
        msg = f"{cidade}, {estado} - população {populacao}".title()
    else:
        msg = f"{cidade}, {estado}".title()
    return msg

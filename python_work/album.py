registros = []


def make_album(artista, album, num_musicas=None):
    dicionario = {"artista": artista, "album": album}
    if num_musicas:
        dicionario["num_musicas"] = num_musicas
    return dicionario


def print_album(album):
    if "num_musicas" in album:
        print(f'Artista: {album["artista"]}, Album: {album["album"]}, Numero de Musicas: {album["num_musicas"]}')
    else:
        print(f'Artista: {album["artista"]}, Album: {album["album"]}')


while True:
    artista = input("Qual o nome do artista? ")
    album = input("Qual o nome do album? ")
    num_musica = input("Qual o numero de musicas do album? Se não desejar adcionar um numero, aperte \"Enter\". ")
    dic_album = make_album(artista, album, num_musica)
    print_album(dic_album)
    continuar = input("Você deseja adcionar mais um resgistro(s/n)? ")
    if continuar.lower() == "n":
        print("Até a proxima!!!")
        break

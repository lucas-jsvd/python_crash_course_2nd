def build_profile(primeiro_nome, ultimo_nome, **descricao):
    print(f'\nNome: {primeiro_nome}')
    print(f'Sobrenome: {ultimo_nome}')
    for campo in descricao:
        print(f'{campo.title()}: {descricao[campo]}')


build_profile("Lucas", "José", cidade="Aracaju, Brasil", idade=27, tamanho=1.87)
build_profile("Simone", "Santos", cidade="Capela, Brasil", idade=50, tamanho=1.65)

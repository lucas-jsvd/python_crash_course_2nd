lista_pessoas = []
pessoa1 = {"primeiro_nome": "Lucas", "segundo_nome": "José", "idade": 27, "cidade": "Aracaju"}
lista_pessoas.append(pessoa1)
pessoa2 =  {"primeiro_nome": "Simone", "segundo_nome": "Santos", "idade": 50, "cidade": "Capela"}
lista_pessoas.append(pessoa2)
pessoa3 =  {"primeiro_nome": "Sonia", "segundo_nome": "Regina", "idade": 60, "cidade": "Barra dos Coqueiros"}
lista_pessoas.append(pessoa3)

for pessoa in lista_pessoas:
    print(f'Nome: {pessoa["primeiro_nome"]},\nSobrenome: {pessoa["segundo_nome"]},\nIdade: {pessoa["idade"]},\nCidade: {pessoa["cidade"]}\n')

convidados = ["Max", "Engels", "Rousseau "]
convidado_excluido = convidados.pop()
convidados.append("Nietzsche")
print(f'Infelizmente o {convidado_excluido} não poderar participar da festa.')
print(f'Convidados, conseguimos encontra um messa de jantar maior.')
convidados.insert(0, "Socrátes")
convidados.insert(int(len(convidados)/2), "Platão")
convidados.append("Aristóteles")
print(f'Ao total temos {len(convidados)}.')
for convidado in convidados:
    msg = f'Olá {convidado} gostaria de convidá-lo para festa de hoje a noite.'
    print(msg)
print("Convidados, infelizmente tivemos um problema com nossa mesa.")
print("Só podemos convidar duas pessoas para a festa.")
for x in range(len(convidados) - 2):
    convidado_excluido = convidados.pop()
    print(
        f'Me desculpe {convidado_excluido}, infelizmente não teremos mais vagas para o jantar.')
for convidado in convidados:
    msg = f'Olá {convidado} gostaria de convidá-lo para festa de hoje a noite.'
    print(msg)
for index in range(len(convidados)):
    convidados.pop()
print(convidados)

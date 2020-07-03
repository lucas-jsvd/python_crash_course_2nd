num_pessoas = input("Você deseja uma mesa para qunatas pessoas ? ")
if int(num_pessoas) <= 8:
    print(f'Nós temos uma mesa para {num_pessoas} pessoas pronta para você.')
else:
    print(f'Nós não temos uma mesa para {num_pessoas} pessoas disponivel no momento.')
    print('Você precisará espera alguns minutos.')

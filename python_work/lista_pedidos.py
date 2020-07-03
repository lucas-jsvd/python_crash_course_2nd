pedidos_sanduiches = ["X-Tudo", "Pastrami","X-Calabresa", "Pastrami", "X-Burguer", "Misto-Quente", "Pastrami"]
sanduiches_prontos = []

print("A lanchonete está sem Pastrami no momento.")
while "Pastrami" in pedidos_sanduiches:
    pedidos_sanduiches.remove("Pastrami")

while pedidos_sanduiches:
    pedido_pronto = pedidos_sanduiches.pop()
    print(f"O pedido do {pedido_pronto} está pronto.")
    sanduiches_prontos.append(pedido_pronto)

print("Os seguintes sanduiches foram feitos hoje: ")
for pedido_pronto in sanduiches_prontos:
    print(f'\t{pedido_pronto}')

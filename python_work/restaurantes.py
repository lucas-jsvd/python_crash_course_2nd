from modulo_restaurante import Restaurante, CarrinhoSorvete

bicho_bruto = Restaurante("Bicho Bruto", "Lanchonete")
print(bicho_bruto.nome, bicho_bruto.cozinha)
bicho_bruto.descricao()
bicho_bruto.aberto()
print(bicho_bruto.num_atendimento)
bicho_bruto.num_atendimento = 15
print(bicho_bruto.num_atendimento)

galegos = Restaurante("Galegos", "Lanchonete")
galegos.descricao()
galegos.set_num_atendimento(26)
print(galegos.num_atendimento)

china_box = Restaurante("China Box", "Chinesa")
china_box.descricao()
china_box.incr_num_atendimento(42)
print(china_box.num_atendimento)

sorvete_da_tia = CarrinhoSorvete("Sorvete da Tia", "Sorveteria")
sorvete_da_tia.descricao()
sorvete_da_tia.exibe_sabores()

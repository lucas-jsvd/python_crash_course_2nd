from modulo_usuario import Usuario
from modulo_administrador import Adminitrador

lucas = Usuario("Lucas", "José", 27, "Masculino", "Aracaju/BR")
simone = Usuario("Simone", "Silva", 50, "Feminino", "Capela/BR")

lucas.bem_vindo()
lucas.descricao()
lucas.incr_tentativa_login()
lucas.incr_tentativa_login()
lucas.incr_tentativa_login()
print(lucas.tentativa_login)
lucas.reset_tentativa_login()
print(lucas.tentativa_login)

simone.bem_vindo()
simone.descricao()
simone.incr_tentativa_login()
simone.incr_tentativa_login()
print(simone.tentativa_login)
simone.reset_tentativa_login()
print(simone.tentativa_login)

dulce = Adminitrador("Dulce", "Santos", 15, "Feminino", "Aracaju/BR")
dulce.descricao()
dulce.privilegios.exibir_previlegios()

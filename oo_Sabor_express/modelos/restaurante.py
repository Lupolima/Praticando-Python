class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Sabor da Praça"
restaurante_praca.categoria = "Comida Caseira"


restaurante_esquina = Restaurante()

restaurantes = [restaurante_praca, restaurante_esquina]

print(restaurante_praca)




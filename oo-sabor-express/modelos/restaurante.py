class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Caseira'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
#print(dir(restaurante_praca))
#print(restaurante_praca.ativo)
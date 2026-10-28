from modelos.restaurante import Restaurante

restaurante_express = Restaurante('Sabor Express', 'Cafeteria')
restaurante_hut = Restaurante('Pizza Hut', 'Pizzaria')
restaurante_king = Restaurante('Burger King', 'Fast Food')

restaurante_express.alternar_estado()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
    
from modelos.restaurante import Restaurante

restaurante_express = Restaurante('Sabor Express', 'Cafeteria')
restaurante_express.receber_avalicao('João', 5)
restaurante_hut = Restaurante('Pizza Hut', 'Pizzaria')
restaurante_hut.receber_avalicao('Maria', 8)
restaurante_king = Restaurante('Burger King', 'Fast Food')
restaurante_king.receber_avalicao('Carlos', 7)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
    
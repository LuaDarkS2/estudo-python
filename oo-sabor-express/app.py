import sys
from modelos.restaurante import Restaurante

sys.stdout.reconfigure(encoding='utf-8')

restaurante_express = Restaurante('Sabor Express', 'Cafeteria')
restaurante_express.receber_avalicao('João', 5)
restaurante_express.receber_avalicao('Ana', 9)
restaurante_express.receber_avalicao('Pedro', 7)
restaurante_hut = Restaurante('Pizza Hut', 'Pizzaria')
restaurante_hut.receber_avalicao('Maria', 8)
restaurante_hut.receber_avalicao('Lucas', 6)
restaurante_king = Restaurante('Burger King', 'Fast Food')
restaurante_king.receber_avalicao('Rafael', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
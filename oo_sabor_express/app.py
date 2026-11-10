import sys
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

sys.stdout.reconfigure(encoding='utf-8')

restaurante_express = Restaurante('Sabor Express', 'Cafeteria')
restaurante_hut = Restaurante('Pizza Hut', 'Pizzaria')
restaurante_king = Restaurante('Burger King', 'Fast Food')

bebiba1 = Bebida('Coca-Cola', 5.0, '500ml')
prato1 = Prato('Pão de Queijo', 3.0, 'Delicioso pão de queijo quentinho')

bebiba1.aplicar_desconto()
prato1.aplicar_desconto()

restaurante_express.adicionar_no_cardapio(bebiba1)
restaurante_express.adicionar_no_cardapio(prato1)

def main():
    restaurante_express.exibir_cardapio

if __name__ == '__main__':
    main()
import sys
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

sys.stdout.reconfigure(encoding='utf-8')

restaurante_express = Restaurante('Sabor Express', 'Cafeteria')
#restaurante_express.receber_avalicao('João', 5)
#restaurante_express.receber_avalicao('Ana', 9)
#restaurante_express.receber_avalicao('Pedro', 7)
restaurante_hut = Restaurante('Pizza Hut', 'Pizzaria')
#restaurante_hut.receber_avalicao('Maria', 8)
#restaurante_hut.receber_avalicao('Lucas', 6)
restaurante_king = Restaurante('Burger King', 'Fast Food')
#restaurante_king.receber_avalicao('Rafael', 8)

bebiba1 = Bebida('Coca-Cola', 5.0, '500ml')
prato1 = Prato('Pão de Queijo', 3.0, 'Delicioso pão de queijo quentinho')

#restaurante_express.adicionar_bebida_no_cardapio(bebiba1)
#restaurante_express.adicionar_prato_no_cardapio(prato1)

restaurante_express.adicionar_no_cardapio(bebiba1)
restaurante_express.adicionar_no_cardapio(prato1)

def main():
    restaurante_express.exibir_cardapio()
    #print(bebiba1)
    #print(prato1)
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
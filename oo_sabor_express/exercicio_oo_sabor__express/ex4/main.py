# exercicio 7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# exercicio 8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

import sys

from carro import Carro
from moto import Moto

sys.stdout.reconfigure(encoding='utf-8')

carro1 = Carro('Toyota', 'Corolla', 4)
carro2 = Carro('Chevrolet', 'Astra', 2)
carro3 = Carro('Honda', 'SUV', 6)
moto1 = Moto('Yamaha', 'R1', 'Esportiva')
moto2 = Moto('Honda', 'CB500', 'Casual')
moto3 = Moto('Vespa', 'Scooter', 'Casual')

# exercicio 9 - Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

def main():
    print(carro1)
    print(carro2)
    print(carro3)
    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == '__main__':
    main() 
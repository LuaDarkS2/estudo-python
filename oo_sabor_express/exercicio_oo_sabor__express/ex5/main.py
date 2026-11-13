#exercicio 5 - Em um arquivo chamado main.py, importe a classe Carro.
#exercicio 6 - No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.


from carro import Carro


carro1 = Carro("Toyota", "Corolla", "Prata", 4)
carro2 = Carro("Honda", "Civic", "Vermelho", 4)
carro3 = Carro("Ford", "Mustang", "Azul", 2)

for carro in (carro1, carro2, carro3):
    print(carro)
    print(carro.ligar())
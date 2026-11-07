# exercicio 5 - Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. 
# Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

# exercicio 6 - Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto 
# que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.

    def __str__(self):
        return f'{super().__str__()} | Tipo: {self._tipo}'

#Foi usado super().__str__() para reaproveitar a descrição já criada na classe Veiculo — marca, modelo e estado — e 
# acrescentar a informação específica da classe filha.

#O super().__str__() chama o __str__ de Veiculo. Depois, a f-string acrescenta o tipo da moto. 
# Assim, imprimir uma moto resulta em algo como:
# Veículo: Yamaha | Modelo: R1 | Estado: desligado | Tipo: Esportiva

#O mesmo princípio vale para Carro, que acrescenta a quantidade de portas. Sem super(), 
# seria preciso repetir na classe filha o código que formata marca, modelo e estado.
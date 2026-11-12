#exercicio 3 - Crie uma nova classe chamada Carro que herda da classe Veiculo.
#exercicio 4 - No construtor da classe Carro, utilize o método super() para chamar 
# o construtor da classe pai e atribua o atributo específico cor à classe filha.


from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor

    def ligar(self):
        return f"{self.marca} {self.modelo} esta ligado."

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Cor: {self.cor} | Portas: {self.portas}"
#Exercicio 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo}, {self.cor}, {self.ano}'

    def listar_carros():
        for carro in Carro.carros:
            print(f'Modelo: {carro.modelo}, Cor: {carro.cor}, Ano: {carro.ano}')

carro1 = Carro('Fusca', 'Azul', 1970)
carro2 = Carro('Gol', 'Prata', 2005)
carro3 = Carro('Civic', 'Preto', 2018)

carros = [carro1, carro2, carro3]

Carro.listar_carros()

#exercicio 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie 
# mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

#exercicio 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e 
# categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

#exercicio 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, 
# seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome}, {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome}, Categoria: {restaurante.categoria}, Ativo: {restaurante.ativo}')


restaurante1 = Restaurante('Pizza Hut', 'Comida Italiana')
restaurante2 = Restaurante('McDonalds', 'Fast Food')
restaurante3 = Restaurante('Sabor Caseiro', 'Comida Caseira')

restaurantes = [restaurante1, restaurante2, restaurante3]

Restaurante.listar_restaurantes()

#exercicio 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 
# objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    clientes = []

    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.ativo = True
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.email}, {self.telefone}'

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'Cliente - Nome: {cliente.nome}, Idade: {cliente.idade}, Email: {cliente.email}, Telefone: {cliente.telefone}, Ativo: {cliente.ativo}')

cliente1 = Cliente('João', 30, 'joao@gmail.com', '123456789')
cliente2 = Cliente('Maria', 22, '', '987654321')
cliente3 = Cliente('Pedro', 28, 'pedro@gmail.com', '')

clientes = [cliente1, cliente2, cliente3]

Cliente.listar_clientes()
#exercício 1 - Python na Escola de Programação da Alura
print('Python na Escola de Programação da Alura.\n')

#exercício 2 - meu nome é {nome} e tenho {anos} anos em que o nome e idade precisam ser valores armazenados em variáveis
nome_aluna = input('Digite seu nome: ')
anos_aluna = input('Digite sua idade: ')
print(f'Meu nome é {nome_aluna} e tenho {anos_aluna} anos.\n')

#exercicio 3 - ALURA de modo que cada letra fique em uma linhas
#a duas formas de fazer isso, uma com o \n e outra com aspas triplas
print('A\nL\nU\nR\nA\n')
print("""A
L
U
R
A
""")

#exercicio 4 - o valor arredondade de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variavel e arredondado para apenas 2 cadas decimais
#para fazer essa conta, é necessário importar a biblioteca math e usar a função pi para pegar o valor de pi
#para ter apenas duas casas decimais, é necessário usar a formatação de string com f-string e o :.2f 
import math
pi = math.pi
print(f'O valor arredondado de pi é: {pi:.2f}\n')

#outra formas de fazer isso, é simplesmente armazenar o valor de pi em uma variavel.
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}\n')
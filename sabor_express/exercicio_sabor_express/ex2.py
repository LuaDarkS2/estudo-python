#exercicio 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o 
#número é par ou ímpar.

import os

def finalizar_app():
    os.system('cls') #limpa a tela do terminal
    print('Encerrando do Aplicativo')
    
def verificar_par_ou_impar():
    numero = int(input('Digite uma numero: '))
    if numero % 2 == 0: #o operador % é o operador de módulo, que retorna o resto da divisão do número por 2. Se o resto for 0, o número é par.
        print(f'O número {numero} é par.')
    else:
        print(f'o número {numero} é impar.')


#exercicio 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em 
#categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

def classificar_idade():
    idade = int(input('Digite sua idade:'))
    if idade >= 0 and idade <= 12:
        print('Você é uma criança.')
    elif idade > 13 and idade <= 18:
        print('Você é um adolescente.')
    else:
        print('Você é um adulto.')



#exercicio 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a 
#senha fornecidos correspondem aos valores esperados determinados por você.

def verificar_usuario_e_senha():
    usuario = input('Digite seu nome de usuário:')
    senha = input('Digite sua senha:')
    if usuario == 'admin' and senha == '1234':
        print('Acesso concedido.')
    else:
        print('Acesso negado.')


#exercicio 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para 
#determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem

def determinar_quadrante():
    x = float(input('Digite a coordenada x:'))
    y = float(input('Digite a coordenada y:'))
    if x > 0 and y > 0:
        print('O ponto está no Primeiro Quadrante.')
    elif x < 0 and y > 0:
        print('O ponto está no Segundo Quadrante.')
    elif x < 0 and y < 0:
        print('O ponto está no Terceiro Quadrante.')
    elif x > 0 and y < 0:
        print('O ponto está no Quarto Quadrante.')
    else:
        print('O ponto está localizado no eixo ou origem.')


def main():
    verificar_par_ou_impar()
    classificar_idade()
    verificar_usuario_e_senha()
    determinar_quadrante()

if __name__ == '__main__':
    main() 

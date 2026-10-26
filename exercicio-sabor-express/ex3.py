#exercicio 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

from ast import main
import os

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Madu', 'Nicolas', 'Gabriel', 'Taynan']
anos = [2004, 2026]


#exercicio 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

def exibir_lista():
    print('Escolha uma das opções abaixo para exibir a lista correspondente:')
    print('1. Acessar lista de numeros')
    print('2. Acessar lista 2 de numeros')
    print('3. Acessar lista de nomes')
    print('4. Acessar lista de anos')
    print('5. Acessar lista de medias')

    print('\nEscolha uma das opções abaixo caso deseje brincar com a lista de numeros:')
    print('6. Calcular a soma dos números ímpares')
    print('7. Imprimir números em ordem decrescente')
    print('8. Imprimir a tabuada de um número')
    print('9. Calcular a soma dos numeros da lista 2')
    print('10. Calcular a média da lista')
    print('11. Calcular a média da lista 2')

    print('\nEscolha essa opção caso deseje sair do programa:')
    print('12. Sair')

def voltar_ao_menu_principal():
    input('Digite para voltar ao menu principal: ')
    main() # chama a função main, que é a função principal do programa, e volta o programa para inicia-lo novamente

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela do terminal
    print(texto)
    print()


def listar_numeros():
    exibir_subtitulo('Listando todos os numeros: ')

    for numero in numeros:
        print(f'{numero}')

    voltar_ao_menu_principal()

def listar_nomes():
    exibir_subtitulo('Listando todos os nomes: ')

    for nome in nomes:
        print(f'{nome}')

    voltar_ao_menu_principal()

def listar_anos():
    exibir_subtitulo('Listando ano de nascimento e ano atual: ')

    for ano in anos:
        print(f'{ano}')   

    voltar_ao_menu_principal()

def escolher_opcao():
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            listar_numeros()
        elif opcao_escolhida == 2:
            listar_numeros2()
        elif opcao_escolhida == 3:
            listar_nomes()
        elif opcao_escolhida == 4:
            listar_anos()
        elif opcao_escolhida == 5:
            listar_medias()
        elif opcao_escolhida == 6:
            calcular_soma_impares()
        elif opcao_escolhida == 7:
            imprimir_numeros_decrescente()
        elif opcao_escolhida == 8:
            imprimir_tabuada()
        elif opcao_escolhida == 9:
            calcular_soma_lista()
        elif opcao_escolhida == 10:
            calcular_media_lista(medias)
        elif opcao_escolhida == 11:
            calcular_media2(medias2)
        elif opcao_escolhida == 12:
            print('Finalizando o programa...')
        else:
            print('Opção inválida!')


#exercicio 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

def calcular_soma_impares():

    soma_impares = 0
    for i in range(1, 11):
        if i % 2 != 0:
            soma_impares += i
    print(f'A soma dos números ímpares de 1 a 10 é: {soma_impares}')

    voltar_ao_menu_principal()


#exercicio 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

def imprimir_numeros_decrescente():
    exibir_subtitulo('Imprimindo números em ordem decrescente: ')

    for i in range(10, 0, -1):
        print(f'{i}')

    voltar_ao_menu_principal()


#exercicio 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir 
# a tabuada desse número, indo de 1 a 10.

def imprimir_tabuada():
    numero = int(input('Digite um número para imprimir a tabuada: '))
    exibir_subtitulo(f'Tabuada do número {numero}: ')

    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')

    voltar_ao_menu_principal()


#exercicio 6 - Crie uma lista de números e utilize um loop for para calcular a soma 
# de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

numeros2 = [ 2, 9, 14, 15, 24, 28, 31, 35, 42, 47]


def listar_numeros2():
    exibir_subtitulo('Listando todos os numeros da lista 2: ')

    for numero2 in numeros2:
        print(f'{numero2}')

    voltar_ao_menu_principal()

def calcular_soma_lista():
    some = 0
    try:
        for numero2 in numeros2:
            some += numero2
            print(f'Soma dos numeros da lista 2: {some}')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    voltar_ao_menu_principal()


#exercicio 7 - Construa um código que calcule a média dos valores em 
# uma lista. Utilize um bloco try-except para lidar com a divisão por 
# zero, caso a lista esteja vazia.

medias = [10, 20, 30, 40, 50]
medias2 = []

def listar_medias():
    exibir_subtitulo('Listando todos os numeros da lista de medias: ')

    for media in medias:
        print(f'{media}')

    voltar_ao_menu_principal()

def calcular_media_lista(lista):
    try:
        media = sum(lista) / len(lista)
        print(f'A média da lista é: {media}')
    except ZeroDivisionError:
        print('Não é possível calcular a média de uma lista vazia.')

def calcular_media2(lista):
    try:
        media2 = sum(lista) / len(lista)
        print(f'A média da lista 2 é: {media2}')
    except ZeroDivisionError:
        print('Não é possível calcular a média de uma lista vazia.')

def main():
    os.system('cls')
    exibir_lista()
    escolher_opcao()

if __name__ == '__main__':
    main() 
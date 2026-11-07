#exercicio 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
import os

quadrados = {i: i**2 for i in range(1, 6)}

def exibir_quadrados():
    print('Dicionário de números e seus quadrados:')
    print('1. Acessar dicionário de quadrados')
    print('2. Sair do programa\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...')

def voltar_ao_menu_principal():
    input('Digite para voltar ao menu principal: ')

def opcao_invalida():
    os.system('cls') #limpa a tela do terminal
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela do terminal
    print(texto)
    print()

def listar_quadrados():
    exibir_subtitulo('Listando números e seus quadrados:')
    for num, quad in quadrados.items():
        print(f'{num} ao quadrado é {quad}')

    voltar_ao_menu_principal()

def escolher_opcao():
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        listar_quadrados()
    elif opcao == 2:
         finalizar_app()
         return False
    else:
        opcao_invalida() 

    return True

def main():
    continuar = True
    while continuar:
        os.system('cls')
        exibir_quadrados()
        continuar = escolher_opcao()   

if __name__ == '__main__':
    main()    
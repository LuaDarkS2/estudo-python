#exercico 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

import os

frequencia_palavras = {'exemplo': 2, 'de': 3, 'frase': 1, 'com': 1, 'palavras': 1}

def exibir_lista():
    print('Dicionário de palavras e suas frequências:')
    print('1. Acessar a frequência do dicionário de palavras')
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

def listar_frequencia():
    exibir_subtitulo('Listando a frequência das palavras: ')

    for palavra, frequencia in frequencia_palavras.items():
        print(f'Palavra: {palavra.ljust(15)} | Frequência: {frequencia}')

    voltar_ao_menu_principal()

def escolher_opcao():
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        listar_frequencia()
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
        exibir_lista()
        continuar = escolher_opcao()

if __name__ == '__main__':
    main()
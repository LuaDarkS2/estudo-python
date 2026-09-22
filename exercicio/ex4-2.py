#exercicio 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

import os

chaves = [ 123456, 789012, 345678, 901234, 567890 ]

def exibir_chaves():
    print('Dicionário de chaves:')
    print('1. Acessar dicionário de chaves')
    print('2. Verificar se uma chave existe')
    print('3. Sair do programa\n')

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

def listar_chaves():
    exibir_subtitulo('Listando todas as chaves: ')

    for chave in chaves:
        print(f'Chave: {chave}')

    voltar_ao_menu_principal()

def verificar_chave():
    exibir_subtitulo('Verificando se uma chave existe: ')
    chave_a_verificar = int(input('Digite a chave a ser verificada: '))

    if chave_a_verificar in chaves:
        print(f'A chave {chave_a_verificar} existe no dicionário.')
    else:
        print(f'A chave {chave_a_verificar} não existe no dicionário.')

    voltar_ao_menu_principal()

def escolher_opcao():
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        listar_chaves()
    elif opcao == 2:
        verificar_chave()
    elif opcao == 3:
         finalizar_app()
         return False
    else:
        opcao_invalida() 

    return True

def main():
    continuar = True
    while continuar:
        os.system('cls')
        exibir_chaves()
        continuar = escolher_opcao()

if __name__ == '__main__':
    main()






from ast import main
import os

restaurantes = ['Pizzaria', 'Hamburgueria', 'Sushi'] # lista vazia para armazenar os restaurantes cadastrados


def exibir_nome_do_programa():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Avaliar restaurante')
    print('4. Sair do Aplicativo\n')

# para definir função, usa-se def
def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...')

def voltar_ao_menu_principal():
    input('Digite para voltar ao menu principal: ')
    main() # chama a função main, que é a função principal do programa, e volta o programa para inicia-lo novamente

def opcao_invalida():
    os.system('cls') #limpa a tela do terminal
    print('Opçãoo Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela do terminal
    print(texto)
    print()

def cadastrar_novo_restaurante():
    os.system('cls') #limpa a tela do terminal
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    restaurantes.append(nome_do_restaurante) # adiciona o nome do restaurante na lista de restaurantes
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes cadastrados')

    for restaurante in restaurantes: # para cada restaurante na lista de restaurantes, vai imprimir o nome do restaurante
        print(f'.{restaurante}') # imprime o nome do restaurante

    voltar_ao_menu_principal()

def escolher_opcao():
    # para transforma em num inteiro, 1 escreve em string, depois tranforma em inteiro
    # usando int antes do input, assim o input vai ser transformado em inteiro, e não mais em string
    try: # tenta executar o código, tentanddo trosformar caso teclem uma letra em numero inteiro, se der erro, vai para o except
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Avaliar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except: 
        opcao_invalida()

def main():
    os.system('cls') #limpa a tela do terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': # nomeia esse arquivo principal
    main() # chama a função main, que é a função principal do programa
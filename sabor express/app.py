from ast import main
import os

restaurantes = [{'nome': 'Massas Divinas', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Burger King', 'categoria': 'Hamburgueria', 'ativo': True},
                {'nome': 'KFC', 'categoria': 'Francesa', 'ativo': False}] 


def exibir_nome_do_programa():
    '''Essa função é responsavel por exibir o nome do programa'''
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    '''Essa função é responsavel por exibir as opções do programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair do Aplicativo\n')

# para definir função, usa-se def
def finalizar_app():
    '''Essa função é responsavel por finalizar o aplicativo'''
    exibir_subtitulo('Finalizando o aplicativo...')

def voltar_ao_menu_principal():
    '''Essa função é responsavel por voltar ao menu principal do programa
    
    Outputs:
    - Retorna ao menu pricipal
    
    '''
    input('Digite para voltar ao menu principal: ')
    main() # chama a função main, que é a função principal do programa, e volta o programa para inicia-lo novamente

def opcao_invalida():
    '''Essa função é responsavel por exibir uma mensagem de erro 
        caso o usuário digite uma opção inválida
        
        Outputs:
        - Retorna ao menu pricipal

    '''
    os.system('cls') #limpa a tela do terminal
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsavel por exibir um subtitulo no programa
    
    Imputs:
    - Texto: str - O texto do subtitulo
    
    '''
    os.system('cls') #limpa a tela do terminal
    linha = '*' * (len(texto)) # cria uma linha de asteriscos com o mesmo tamanho do texto, len = tamanho
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante.
    
    Imputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes

    ''' 
    os.system('cls') #limpa a tela do terminal
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} # cria um dicionário com os dados do restaurante
    restaurantes.append(dados_do_restaurante) # adiciona o dicionário do restaurante na lista de restaurantes

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavel por listar informaçoes dos restaurantes cadastrados.
    
    Outputs:
    - Exibe a lista de restaurantes na tela

    '''
    exibir_subtitulo('Listando restaurantes cadastrados')

    print(f' {'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}') # imprime o cabeçalho da tabela


    for restaurante in restaurantes: # para cada restaurante na lista de restaurantes, vai imprimir o nome do restaurante
        nome_restaurante = restaurante['nome'] # pega o nome do restaurante
        categoria = restaurante['categoria'] # pega a categoria do restaurante
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado' # pega se o restaurante está ativo ou não
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') # imprime o nome do restaurante

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsavel por alternar o estado do restaurante.
    
    Outputs:
    - Exibe mensagem indicando o sucesso da opreção
    
    '''
    exibir_subtitulo('Alternando o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False # cria uma variável para verificar se o restaurante foi encontrado

    for restaurante in restaurantes: # para cada restaurante na lista de restaurantes, vai verificar se o nome do restaurante é igual ao nome do restaurante que deseja alterar o estado
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True # se o restaurante for encontrado, a variável restaurante_encontrado é alterada para True
            restaurante['ativo'] = not restaurante['ativo'] # altera o estado do restaurante para o contrário do estado atual
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso' 
            print(mensagem)

    if not restaurante_encontrado: # se o restaurante não for encontrado, a variável restaurante_encontrado é False
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsavel por escolher a opção do menu principal do programa.
    
    Outputs:
    - Chama a função correspondente a opção escolhida pelo usuário
    
    '''
    # para transforma em num inteiro, 1 escreve em string, depois tranforma em inteiro
    # usando int antes do input, assim o input vai ser transformado em inteiro, e não mais em string
    try: # tenta executar o código, tentanddo trosformar caso teclem uma letra em numero inteiro, se der erro, vai para o except
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except: 
        opcao_invalida()

def main():
    '''Essa função é responsavel por iniciar o programa.'''
    os.system('cls') #limpa a tela do terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': # nomeia esse arquivo principal
    main() # chama a função main, que é a função principal do programa
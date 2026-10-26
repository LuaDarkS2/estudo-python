#exercicio 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

import os

pessoas = [
    {
        'nome': 'Madu',
        'idade': 22,
        'cidade': 'Espirito Santo do Pinhal'
    },
    {
        'nome': 'Nicolas',
        'idade': 21,
        'cidade': 'Espirito Santo do Pinhal'
    },
    {
        'nome': 'Taynan',
        'idade': 23,
        'cidade': 'Espirito Santo do Pinhal',
    }
]

#exercicio 2 - Utilizando o dicionário criado no item 1:

    #Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    #Adicione um campo de profissão para essa pessoa;
    #Remova um item do dicionário.


def exibir_lista():
    print('Escolha uma das opções abaixo para exibir dicionario:')
    print('1. Acessar lista de pessoas')
    print('2. Adicionar um novo campo')
    print('3. Modificar um campo')
    print('4. Remover um campo')
    print('5. Sair do programa\n')


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


def listar_pessoas():
    exibir_subtitulo('Listando todas as pessoas: ')

    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        profissao = pessoa.get('profissao', 'Não informado')
        print(f'Nome: {nome.ljust(10)} | Idade: {str(idade).ljust(5)} | '
              f'Cidade: {cidade.ljust(20)} | Profissão: {profissao}')

    voltar_ao_menu_principal()

def adicionar_campo():
    exibir_subtitulo('Adicionando um novo campo: ')

    for pessoa in pessoas:
        nome = pessoa['nome']
        profissao = input(f'Digite a profissão de {nome}: ')
        pessoa['profissao'] = profissao
        

    print('Campo adicionado com sucesso!')
    voltar_ao_menu_principal()

def modificar_campo():
    exibir_subtitulo('Modificando um campo: ')

    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = input(f'Digite a nova idade de {nome}: ')
        pessoa['idade'] = idade

    print('Campo modificado com sucesso!')
    voltar_ao_menu_principal()

def remover_campo():
    exibir_subtitulo('Removendo um campo: ')

    for pessoa in pessoas:
        nome = pessoa['nome']
        if 'profissao' in pessoa:
            del pessoa['profissao']
            print(f'Campo profissão removido de {nome}.')
        else:
            print(f'{nome} não possui o campo profissão.')

    voltar_ao_menu_principal()

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))

    if opcao_escolhida == 1:
        listar_pessoas()
    elif opcao_escolhida == 2:
        adicionar_campo()
    elif opcao_escolhida == 3:
        modificar_campo()
    elif opcao_escolhida == 4:
        remover_campo()
    elif opcao_escolhida == 5:
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
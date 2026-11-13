# exercicio 1 - Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
# Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
      
# exercicio 2 - Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor 
# e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano: {self._ano_publicacao}'

# exercicio 3 - Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def emprestar(self):
        self._disponivel = False

# exercicio 4 - Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro 
# e retorna uma lista dos livros disponíveis publicados nesse ano.

    @staticmethod
    def verificar_disponibilidade(ano):
        return [
            livro for livro in Livro.livros
            if livro._ano_publicacao == ano and livro._disponivel
        ]

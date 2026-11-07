# exercicio 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from ex3 import Livro

# exercicio 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o 
# livro está disponível ou não após o empréstimo.

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)
livro2 = Livro("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005)
livro3 = Livro("A menina que Roubava Livros", "Markus Zusak", 2005)
livro4 = Livro("Crepusco", "Stephenie Meyer", 2005)
livro5 = Livro("Maze Runner: Correr ou Morrer", "James Dashner", 2009)
livro6 = Livro("A culpa é das estrelas", "John Green", 2012)

print(livro1)
print(livro2)
print(livro3)
print(livro4)
print(livro5)
print(livro6)

livro3.emprestar()
print()
print(f'O livro "{livro3._titulo}" está disponível: {livro3._disponivel if livro3._disponivel else "Não"}')

Livro.livros = [livro1, livro2, livro3, livro4, livro5, livro6]

livro6.emprestar()
print()
print(f'O livro "{livro6._titulo}" está disponível: {livro6._disponivel if livro6._disponivel else "Não"}')

# exercicio 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros 
# disponíveis publicados em um ano específico.

ano_especifico = int(input("Digite o ano de publicação: "))
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
if livros_disponiveis_ano:
    print(f"Livros disponíveis publicados em {ano_especifico}:")
    for livro in livros_disponiveis_ano:
        print(livro)
else:
    print(f"Nenhum livro disponível publicado em {ano_especifico}.")

from amigo import Amigo
from livro import Livro
from bibliotecapessoal import BibliotecaPessoal
from datetime import datetime

livro1 = Livro("Python para iniciantes", "O básico de Python", "Rei do Python", "Linguagem Python", "Educação", "maiores de 12 anos")
livro2 = Livro("Java para iniciantes", "O básico de Java", "Rei do Java", "Linguagem Java", "Educação", "maiores de 30 anos")
livro3 = Livro("C para iniciantes", "O básico de C", "Rei do C", "Linguagem C", "Educação", "maiores de 18 anos")
livro4 = Livro("C++ para iniciantes", "O básico de C++", "Rei do C++", "Linguagem C++", "Educação", "maiores de 12 anos")

amigo1= Amigo("Rodrigo", ["40028922"], "rodrigo@gmail.com")
amigo2 = Amigo("Pedro", ["40558922"], "pedro@gmail.com")
amigo3 = Amigo("Lucas", ["40023322"], "lucas@gmail.com")

biblioteca = BibliotecaPessoal()


biblioteca.adiciona_amigo(amigo1)
biblioteca.adiciona_amigo(amigo2)
biblioteca.adiciona_amigo(amigo3)

biblioteca.adiciona_livro(livro1)
biblioteca.adiciona_livro(livro2)
biblioteca.adiciona_livro(livro3)
biblioteca.adiciona_livro(livro4)

biblioteca.empresta_livro(amigo1, livro1, datetime.now())
biblioteca.ver_livros_emprestados()

biblioteca.empresta_livro(amigo2, livro2, datetime.now())
biblioteca.empresta_livro(amigo3, livro3, datetime.now())

biblioteca.ver_livros_emprestados()

biblioteca.devolve_livro(livro4, datetime.now())
biblioteca.ver_livros_emprestados()

biblioteca.empresta_livro(amigo1, livro1, datetime.now())
biblioteca.ver_livros_emprestados()
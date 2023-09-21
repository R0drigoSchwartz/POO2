from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro):
        if isinstance(livro, Livro):
            if not livro in self.livros and livro != None:
                self.livros.append(livro)

    def excluirLivro(self, livro):
        if isinstance(livro, Livro):
            if livro in self.livros and livro != None:
                self.livros.remove(livro)

    @property
    def livros(self):
        return self.__livros

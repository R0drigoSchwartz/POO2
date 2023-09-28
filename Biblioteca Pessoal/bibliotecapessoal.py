from amigo import Amigo
from livro import Livro
from emprestimo import Emprestimo
from datetime import datetime

class BibliotecaPessoal:
    def __init__(self):
        self.__amigos = []
        self.__livros = []
        self.__emprestimos = []

    @property
    def amigos(self):
        return self.__amigos
    
    @property
    def livros(self):
        return self.__livros
    
    @property
    def emprestimos(self):
        return self.__emprestimos
    
    def adiciona_amigo(self, amigo):
        if isinstance(amigo, Amigo):
            self.amigos.append(amigo)
        else:
            print("O parâmetro passado não é uma instância da classe Amigo")

    def adiciona_livro(self, livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            print("O parâmetro não foi passado corretamente!")

    def empresta_livro(self, amigo, livro, data_inicio):
        if isinstance(amigo, Amigo) and isinstance(livro, Livro) and isinstance(data_inicio, datetime):
            if livro not in self.livros:
                emprestimo = Emprestimo(amigo, livro, data_inicio)
                self.emprestimos.append(emprestimo)
            else:
                print("Este livro já está emprestado")
        else:
            print("Os parâmetros não foram passados corretamente!")
    
    def ver_livros_emprestados(self):
        string_aux = ""
        for i in range(len(self.emprestimos)-1):
            string_aux += self.emprestimos[i].livro.titulo +", "
        string_aux += self.emprestimos[len(self.emprestimos)-1].livro.titulo
        print(f"Os livros emprestados são: {string_aux}")

    def devolve_livro(self, livro, data_fim):
        if isinstance(livro, Livro) and isinstance(data_fim, datetime):
            cont = 0
            for emprestimos in self.emprestimos:
                if emprestimos.ativo:
                    self.emprestimos.remove(emprestimos)
                    livro.data_fim = data_fim
                    return
                cont +=1
            if cont == len(self.emprestimos):
                print("Não é possível devolver um livro que não foi emprestado")
        else:
            print("Os parâmetros não foram passados corretamente")


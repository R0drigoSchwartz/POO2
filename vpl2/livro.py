from editora import Editora
from autor import Autor 
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(ano, int):
            self.__ano = ano
        if isinstance(autor, Autor):
            self.__autores = [autor]
        if isinstance(numeroCapitulo, int):
            if isinstance(tituloCapitulo, str):
                self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
        
    @property
    def ano(self):
        return self.__ano
        
    @property
    def editora(self):
        return self.__editora
    
    @property
    def autores(self):
        return self.__autores
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
    
    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano
    
    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora
            
    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor != None and not autor in self.__autores:
                self.__autores.append(autor)
    
    def excluirAutor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor != None and autor in self.__autores:
                self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        if not self.findCapituloByTitulo(tituloCapitulo) in self.__capitulos:
            if isinstance(numeroCapitulo, int):
                if isinstance(tituloCapitulo, str):
                    self.__capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))
        
    def excluirCapitulo(self, tituloCapitulo: str):
        if self.findCapituloByTitulo(tituloCapitulo) in self.__capitulos:
                if isinstance(tituloCapitulo, str):
                    self.__capitulos.remove(self.findCapituloByTitulo(tituloCapitulo))

    def findCapituloByTitulo(self, tituloCapitulo: str):
        if isinstance(tituloCapitulo, str):
            for capitulos in self.__capitulos:
                if tituloCapitulo == capitulos.titulo:
                    return capitulos
        return None

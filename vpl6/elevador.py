from abstractElevador import AbstractElevador
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahVazioException import ElevadorJahVazioException
from elevadorCheioException import ElevadorCheioException

class Elevador(AbstractElevador):
    def __init__(self):
        super().__init__() 
        self.__andarAtual = 0
        self.__totalAndaresPredio = 0
        self.__capacidade = 0
        self.__totalPessoas = 0
    
    def subir(self):
        if self.andarAtual == self.totalAndaresPredio -1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.andarAtual += 1
    
    def descer(self):
        if self.andarAtual == 0:
            raise ElevadorJahNoTerreoException
        else:
            self.andarAtual -= 1
    
    def entraPessoa(self):
        if self.totalPessoas == self.capacidade:
            raise ElevadorCheioException
        else:
            self.totalPessoas += 1
    
    def saiPessoa(self):
        if self.totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.totalPessoas -= 1
    
    @property
    def andarAtual(self):
        return self.__andarAtual
    
    @property
    def totalAndaresPredio(self):
        return self.__totalAndaresPredio
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property
    def totalPessoas(self):
        return self.__totalPessoas
    
    @andarAtual.setter
    def andarAtual(self, andarAtual: int):
        self.__andarAtual = andarAtual
    
    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio
    
    @totalPessoas.setter
    def totalPessoas(self, totalPessoas: int):
        self.__totalPessoas = totalPessoas
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade




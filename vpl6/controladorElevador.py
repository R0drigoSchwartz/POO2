from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        super().__init__()
        self.__elevador = Elevador()
    
    def subir(self):
        return self.elevador.subir()
        
    def descer(self):
        return self.elevador.descer()
        
    def entraPessoa(self):
        return self.elevador.entraPessoa()

    def saiPessoa(self):
        return self.elevador.saiPessoa()    

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        if isinstance(totalAndaresPredio, int) and totalAndaresPredio >= 0:
            self.elevador.totalAndaresPredio = totalAndaresPredio
        else:
            raise ComandoInvalidoException
        if isinstance(andarAtual, int) and andarAtual >= 0 and andarAtual < self.elevador.totalAndaresPredio:
            self.elevador.andarAtual = andarAtual
        else:
            raise ComandoInvalidoException
        if isinstance(capacidade, int) and capacidade > 0:
            self.elevador.capacidade = capacidade
        else:
            raise ComandoInvalidoException
        if isinstance(totalPessoas, int) and totalPessoas >= 0 and totalPessoas <= self.elevador.capacidade:
            self.elevador.totalPessoas = totalPessoas
        else:
            raise ComandoInvalidoException
            

    @property
    def elevador(self):
        return self.__elevador    

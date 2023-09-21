from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        super().__init__()
        self.__clientes = []
        self.__tecnicos = []
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiClientes(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.clientes.append(cliente)
            return cliente #duvida - olhar a classe controladorabstrata
    
    def incluiTecnico(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            self.tecnicos.append(tecnico)
            return tecnico #duvida - olhar a classe controladorabstrata
    
    



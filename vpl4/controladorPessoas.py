from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str):
        cont = 0
        for cliente in self.clientes:
            if codigo == cliente.codigo:
                cont += 1
        if cont == 0:
            cliente = Cliente(nome, codigo)
            self.clientes.append(cliente)
            return cliente 

    def incluiTecnico(self, codigo: int, nome: str):
        cont = 0
        for tecnico in self.tecnicos:
            if codigo == tecnico.codigo:
                cont += 1
        if cont == 0:
            tecnico = Tecnico(nome, codigo)
            self.tecnicos.append(tecnico)
            return tecnico 




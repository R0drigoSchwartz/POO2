from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, codigo: int):
        self.__codigo = codigo
        super().__init__(nome)
    
    @property
    def codigo(self):
        return self.__codigo
    
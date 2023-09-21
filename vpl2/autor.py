class Autor:
    def __init__(self, codigo:int, nome:str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(nome, str):
            self.__nome = nome
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @codigo.setter
    def codigo(self, codigo:int):
        self.__codigo = codigo
    
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome
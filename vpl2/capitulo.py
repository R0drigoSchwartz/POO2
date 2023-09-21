class Capitulo:
    def __init__(self, numero: int, titulo: str):
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(titulo, str):
                self.__titulo = titulo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titulo(self):
        return self.__titulo
    
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero
    
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
        

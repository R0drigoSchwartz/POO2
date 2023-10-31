from AbstractPersonagem import AbstractPersonagem
from AbstractPersonagem import Tipo

class Personagem(AbstractPersonagem):
    def __init__(self, tipo: Tipo, energia: int, habilidade: int, velocidade: int, resistencia: int):
        super().__init__()
        self.__tipo = tipo
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def energia(self):
        return self.__energia
    
    @property
    def habilidade(self):
        return self.__habilidade
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def resistencia(self):
        return self.__resistencia
        
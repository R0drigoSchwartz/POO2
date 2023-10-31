from AbstractMesa import AbstractMesa
from Carta import *
from Jogador import *

class Mesa(AbstractMesa):
    def __init__(self, jogador1: Jogador, jogador2: Jogador):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2

    @property
    def jogador1(self):
        return self.__jogador1
    
    @property
    def jogador2(self):
        return self.__jogador2
    
    def carta_jogador1(self):
        carta_baixada = self.jogador1.baixa_carta_da_mao()
        return carta_baixada
    
    def carta_jogador2(self):
        carta_baixada = self.jogador2.baixa_carta_da_mao()
        return carta_baixada
    
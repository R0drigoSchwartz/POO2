from AbstractJogador import AbstractJogador
from Carta import *
from POO2.vpl5.Carta import Carta
import random

class Jogador(AbstractJogador):
    def __init__(self, nome: str):
        super().__init__()
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def mao(self):
        return self.__mao
    
    def baixa_carta_da_mao(self):
        carta = random.choice(self.mao)
        self.mao.remove(carta)
        return carta    

    def inclui_carta_na_mao(self, carta: Carta):
        self.mao.append(carta)

    

    

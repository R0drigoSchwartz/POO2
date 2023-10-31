from AbstractControladorJogo import AbstractControladorJogo
from POO2.vpl5.Carta import Carta, Personagem
from POO2.vpl5.Jogador import Carta, Personagem
from POO2.vpl5.Mesa import Carta, Personagem
from POO2.vpl5.Personagem import Personagem
from Personagem import *
from Jogador import *
from Mesa import *
from Carta import *

class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        super().__init__()
        self.__personagens = []
        self.__baralho = []

    @property
    def personagens(self):
        return self.__personagens

    @property
    def baralho(self):
        return self.__baralho
    
    def inclui_personagem_na_lista(self, energia: int, habilidade: int, velocidade: int, resistencia: int, tipo: Tipo):
        personagem = Personagem(tipo, energia, habilidade, velocidade, resistencia)
        self.personagens.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem):
        carta = Carta(personagem)
        self.baralho.append(carta)
        return carta
    
    def jogada(self, mesa: Mesa):
       carta1: Carta = mesa.carta_jogador1
       carta2: Carta = mesa.carta_jogador2
       jogador1: Jogador = mesa.jogador1
       jogador2: Jogador = mesa.jogador2
        if carta1.valor_total_carta() 
        
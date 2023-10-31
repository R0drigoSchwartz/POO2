from AbstractCarta import AbstractCarta
from Personagem import *

class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        super().__init__()
        self.__personagem = personagem
    
    @property
    def personagem(self):
        return self.__personagem
    
    def valor_total_carta(self):
        valor_total = 0
        valor_total = self.personagem.energia + self.personagem.habilidade + self.personagem.resistencia + self.personagem.tipo + self.personagem.velocidade
        return valor_total
    

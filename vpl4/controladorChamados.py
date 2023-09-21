from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        super().__init__()
        self.__chamados = []
        self.__Tiposchamado = []

    @property
    def tiposChamados(self):
        return self.__Tiposchamado

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        if isinstance(tipo, TipoChamado):
            return tipo.chamados
    
    def incluiChamado(self, chamado: Chamado):
        if isinstance(chamado, Chamado):
            self.__chamados.append(chamado)
            return chamado
    
    def incluiTipoChamado(self, tipochamado: TipoChamado):
        if isinstance(tipochamado, TipoChamado):
            self.Tiposchamado.append(tipochamado)
            return tipochamado
    


from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipoChamados = []

    @property
    def tipoChamados(self):
        return self.__tipoChamados
    
    @property
    def chamados(self):
        return self.__chamados

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        if isinstance(tipo, TipoChamado):
            lista = []
            for chamado in self.chamados:
                if tipo == chamado.tipo:
                    lista.append(chamado.tipo)
            return len(lista)

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
            if (isinstance(data, Date) and
            isinstance(cliente, Cliente) and
            isinstance(tecnico, Tecnico) and
            isinstance(tipo, TipoChamado)):
                for chamado in self.chamados:
                    if data == chamado.data and cliente == chamado.cliente and tecnico == chamado.tecnico and tipo == chamado.tipo:
                        return None
                chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
                self.chamados.append(chamado)
                return chamado
                
    
    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str):
        cont = 0
        for tipoChamado in self.tipoChamados:
            if codigo == tipoChamado.codigo:
                cont += 1
        if cont == 0:
            tipochamado = TipoChamado(codigo, descricao, nome)
            self.tipoChamados.append(tipochamado)
            return tipochamado
        else:
            return None
    


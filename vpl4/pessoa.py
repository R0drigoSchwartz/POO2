from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
        
    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo
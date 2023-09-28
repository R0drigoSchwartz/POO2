class Amigo:
    def __init__(self, nome: str, telefone: list, email: str):
        self.__nome = nome
        self.__telefone = [telefone]
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def email(self):
        return self.__email
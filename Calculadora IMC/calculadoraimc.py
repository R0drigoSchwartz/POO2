class CalculadoraIMC:
    def __init__(self, peso: float, altura: float):
        self.__peso = peso
        self.__altura = altura
        self.__imc = 0
    
    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura
    
    @property
    def imc(self):
        return self.__imc

    def calcular_imc(self):
        novo_imc = self.peso / (self.altura/100) ** 2
        self.__imc = round(novo_imc, 1)

    def avaliacao_imc(self):
        if self.imc < 18.5:
            return 'baixo peso'
        elif self.imc >= 18.5 and self.imc <= 24.9:
            return 'peso normal'
        elif self.imc >= 25 and self.imc <= 29.9:
            return 'sobrepeso'
        elif self.imc >= 30 and self.imc <= 34.9:
            return 'obesidade classe I'
        elif self.imc >= 35 and self.imc <= 39.9:
            return 'obesidade classe II'
        else:
            return 'obesidade classe III'


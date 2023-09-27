import PySimpleGUI as sg
from calculadoraimc import CalculadoraIMC

class Interface:
    def __init__(self):
        self.__formato = [
            [sg.Text('Qual seu peso?'), sg.InputText("", key='peso'), sg.Text('Kg')],
            [sg.Text('Qual a sua altura?'), sg.InputText("", key='altura'), sg.Text('cm')],
            [sg.Text("", key='situacao', size=(50, 1))],
            [sg.Text("", size=(14, 1)), sg.Button('Calcular IMC')]
        ]

        self.__window = sg.Window('Calculadora de IMC', self.__formato, font=('Helvetica', 14))
    
    def main(self):
        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Calcular IMC':
                peso = values['peso']
                altura = values['altura']
                if peso.strip() == "" or altura.strip() == "":
                    sg.popup_error('Os campos de peso e altura devem ser preenchidos!')
                elif peso.isalpha() or altura.isalpha():
                    sg.popup_error('Os campos de peso e altura devem conter apenas números!')
                else:
                    peso = float(peso)
                    altura = float(altura)
                    calculadora = CalculadoraIMC(peso, altura)
                    calculadora.calcular_imc()
                    self.__window.Element('situacao').Update(f" O usuário está com {calculadora.avaliacao_imc()}")

        self.__window.close()








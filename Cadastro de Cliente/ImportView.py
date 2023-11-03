import PySimpleGUI as sg

class ImportView:
    def __init__(self, controlador):
        self.__contralador = controlador
        self.__container = []
        self.__window = self.__window = sg.Window("Importação de clientes", self.__container, font=("Helvetica", 14))

    def tela_consulta(self):
        self.__container = [
        [sg.InputText(key="importar")],
        [sg.Button("Importar")]
        ]
        
        self.__window = sg.Window("Importação de clientes", self.__container, font=("Helvetica", 14))

    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        return self.__window.close()

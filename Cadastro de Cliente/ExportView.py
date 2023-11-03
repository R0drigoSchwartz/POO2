from ClienteController import ClienteController
import PySimpleGUI as sg

class ExportView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Exportação de clientes", self.__container, font=("Helvetica", 14))
    
    def tela_consulta(self):
        self.__container = [
        [sg.Text("Digite o nome do arquivo que quer salvar:")],
        [sg.InputText(key="nome_exportar")],
        [sg.Button("Exportar")]
        ]
        
        self.__window = sg.Window("Exportação de clientes", self.__container, font=("Helvetica", 14))

    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        return self.__window.close()


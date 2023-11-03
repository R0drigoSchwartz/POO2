import PySimpleGUI as sg

class ClienteView:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Consulta de Clientes", self.__container, font=("Helvetica", 14))
    
    def tela_consulta(self):
        self.__container = [
                [sg.Text("Digite o código ou o nome do cliente e clique na ação desejada", font=("Helvetica", 15), pad=(65,0))],
                [sg.Text("")],
                [sg.Text("Nome:"), sg.InputText("", key="nome", pad=(15, 0))],
                [sg.Text("Código:"), sg.InputText("", key="codigo")],
                [sg.Text("")],
                [sg.Button("Cadastrar", pad=(10, 0)), sg.Button("Consultar", pad=(10,0)), sg.Button("Remover", pad=(10,0)), sg.Button("Listar Clientes", pad=(10,0)), sg.Button("Exportar", pad=(10, 0)), sg.Button("Importar", pad=(10, 0))],
                [sg.Text("")],
                [sg.Text("", key="resultado")]
            ]
        self.__window = sg.Window("Consulta de Clientes", self.__container, font=("Helvetica", 14))
        

    def mostra_resultado(self, resultado):
        return self.__window.Element("resultado").Update(resultado)

    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        return self.__window.close()
    
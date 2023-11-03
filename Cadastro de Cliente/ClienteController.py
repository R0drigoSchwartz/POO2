from ClienteDAO import ClienteDAO
from ClienteView import ClienteView
from Cliente import Cliente
from ImportView import ImportView
from ExportView import ExportView
import PySimpleGUI as sg

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clienteDAO = ClienteDAO()
        self.__telaExport = ExportView(self)
        self.__telaImport = ImportView(self)
    
    def inicia(self):
        #inicia a tela de consulta
        self.__telaCliente.tela_consulta() 

        #loop de eventos
        rodando = True
        resultado = ""
        while rodando:
            event, values = self.__telaCliente.le_eventos() #le qualquer evento que aconteça na tela

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == "Cadastrar":
                resultado = self.adiciona_cliente(values["nome"], values["codigo"])
                                
            elif event == "Consultar":
                resultado = self.busca_codigo(values["codigo"])
            
            elif event == "Remover":
                resultado = self.remove_cliente(values["nome"], values["codigo"])
            
            elif event == "Listar Clientes":
                resultado = self.listar_clientes()
            
            elif event == "Importar":
                resultado = self.handle_import()
            
            elif event == "Exportar":
                self.handle_export()


            if resultado != "":
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)
        
        self.__telaCliente.fim()

    #busca um cliente com o codigo passado no dict, e retorna ele se existir
    def busca_codigo(self, codigo: str): 
        if not codigo.isdigit():
            return "O código deve ser um número!"
        try:
            self.__clienteDAO.get(codigo) 
            return f"Nome: {self.__clienteDAO.cache[codigo].nome}" 
        except KeyError:
            return "Não há nenhum cliente cadastrado com esse código"  

    #cria novo OBJ cliente e adiciona ao dict, cuja chave e o codigo
    def adiciona_cliente(self, nome: str, codigo: str):
        if nome == "" or nome.isdigit() or not codigo.isdigit():
            return "Os campos devem ser preenchidos corretamente!"
        if codigo not in self.__clienteDAO.cache:
            self.__clienteDAO.add(Cliente(nome, codigo))
            return "Cliente cadastrado!"
        return "Já há um cliente cadastrado com esse código!"
    
    #remove cliete do dict, caso exista
    def remove_cliente(self, nome: str, codigo: str):
        if nome == "" or nome.isdigit() or not codigo.isdigit():
            return "Os campos devem ser preenchidos corretamente!"
        self.__clienteDAO.remove(codigo)
        return "Cliente Removido!"

    def listar_clientes(self):
        str_aux = ""
        if len(self.__clienteDAO.cache) == 0:
            return "Nenhum cliente cadastrado"
        for key in self.__clienteDAO.cache:
            str_aux += f"Cliente: {self.__clienteDAO.cache[key].nome}, código: {key}\n"
        return str_aux

    def handle_import(self):
        self.__telaImport.tela_consulta()

        import_ativa = True

        while import_ativa:
            event_import, values_import = self.__telaImport.le_eventos()

            if event_import == sg.WIN_CLOSED:
                self.__telaImport.fim()
                import_ativa = False
            
            elif event_import == "Importar":
                path = values_import["importar"]
                self.__clienteDAO.import_source(path)
                self.__telaImport.fim()
                import_ativa = False
    
    def handle_export(self):
        self.__telaExport.tela_consulta()

        export_ativa = True

        while export_ativa:
            event_export, event_values = self.__telaExport.le_eventos()

            if event_export == sg.WIN_CLOSED:
                self.__telaExport.fim()
                export_ativa = False
            
            elif event_export == "Exportar":
                path = event_values["caminho_exportar"]
                self.__clienteDAO.set_data_source(path)
                self.__telaExport.fim()
                export_ativa = False           




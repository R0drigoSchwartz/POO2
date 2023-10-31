from ClienteDAO import ClienteDAO
from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clienteDAO = ClienteDAO()
    
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

            if resultado != "":
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)
        
        self.__telaCliente.fim()

    def busca_codigo(self, codigo: str):
        if not codigo.isdigit():
            return "O código deve ser um número!"
        for key in self.__clienteDAO.cache:
           if key == codigo:
                return f"Nome: {self.__clienteDAO.cache[key].nome}"
        return "Não há nenhum cliente cadastrado com esse código"

    #cria novo OBJ cliente e adiciona ao dict, cuja chave e o codigo
    def adiciona_cliente(self, nome: str, codigo: str):
        if nome == "" or nome.isdigit() or not codigo.isdigit():
            return "Os campos devem ser preenchidos corretamente!"
        else:
            if codigo not in self.__clienteDAO.cache:
                self.__clienteDAO.add(Cliente(nome, codigo))
                return "Cliente cadastrado!"
            return "Já há um cliente cadastrado com esse código!"
        
    def remove_cliente(self, nome: str, codigo: str):
        if nome == "" or nome.isdigit() or not codigo.isdigit():
            return "Os campos devem ser preenchidos corretamente!"
        else:
            self.__clienteDAO.remove(codigo)
            return "Cliente Removido!"
    
    def listar_clientes(self):
        str_aux = ""
        if len(self.__clienteDAO.cache) == 0:
            return "Nenhum cliente cadastrado"
        for key in self.__clienteDAO.cache:
            str_aux += f"Cliente: {self.__clienteDAO.cache[key].nome}, código: {key}\n"
        return str_aux
           

    




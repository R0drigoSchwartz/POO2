from DAO import DAO
from Cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__("clientes.pkl")
        
    def add(self, cliente: Cliente):
        if isinstance(cliente.codigo, str) and isinstance(cliente, Cliente):
            super().add(cliente.codigo, cliente)

    def remove(self, key):
        if isinstance(key, str):
            super().remove(key)

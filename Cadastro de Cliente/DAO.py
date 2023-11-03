from abc import ABC
import pickle   

class DAO(ABC):
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        f = open(self.__datasource, "wb")
        pickle.dump(self.__cache, f)
        f.close()

    def __load(self):
        f = open(self.__datasource, "rb")
        self.__cache = pickle.load(f)
        f.close()

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            self.__cache[key]
        except KeyError:
            raise KeyError
    
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
           raise KeyError

    #passa os clientes cadastrados para um arquivo .pkl para ser exportado 
    def set_data_source(self, path):
        if ".pkl" not in path:
            path += ".pkl"
        f = open(path, "wb")
        pickle.dump(self.__cache, f)
        f.close()

    #lê os clientes que estão no arquivo e passa eles para o dict cache
    def import_source(self, path):
        if ".pkl" in path:
            f = open(path, "rb")
            arq = pickle.load(f)
            f.close()
            for cliente in arq.values():
                self.__cache[cliente.codigo] = cliente
            self.__dump()
        
        
    @property
    def cache(self):
        return self.__cache

    
   
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

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
           raise KeyError
        
    @property
    def cache(self):
        return self.__cache
    
   
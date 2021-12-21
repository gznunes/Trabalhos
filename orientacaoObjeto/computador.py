from abc import ABCMeta, abstractmethod, abstractproperty


class Computador(metaclass=ABCMeta):

    @property
    @abstractproperty
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass

    @property
    @abstractproperty
    def cor(self):
        pass

    @cor.setter
    @abstractmethod
    def cor(self, valor):
        pass

    @property
    @abstractproperty
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass

    @abstractmethod
    def cadastrar(self):
        pass

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco
        


    

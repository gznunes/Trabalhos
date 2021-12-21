from computador import Computador

class Notebook (Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):        
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self.__tempoDeBateria = tempoDeBateria


    @property
    def modelo(self):
        return self._modelo
        
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def cor(self):
        return self._cor
        
    @cor.setter
    def cor(self, valor):
        self._cor = valor
    
    @property
    def preco(self):
        return self._preco
        
    @preco.setter
    def preco(self, valor):
        self._preco = valor

    def cadastrar(self):
        print( "O notebook ", self.modelo , " de preço " , self.preco , " foi cadastrado!")

    def getInformacoes(self):
        
        return super().getInformacoes(), self.__tempoDeBateria
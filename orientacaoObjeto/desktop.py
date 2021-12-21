from computador import Computador

class Desktop (Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):        
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self.potenciaDaFonte = potenciaDaFonte


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
        print( "O desktop ", self.modelo , " de preço " , self.preco , " foi cadastrado!")

    def getInformacoes(self):
        super().getInformacoes()
        return super().getInformacoes(), self.potenciaDaFonte

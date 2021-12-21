from No import No

class Pilha:

	def __init__(self):
		self.topo = None
		self.tamanho = 0
		
	
	def empilhar(self, valor) :
		no = No(valor)
		if self.topo != None:
			no.proximo = self.topo
		self.topo = no
		self.tamanho +=1
		

	def imprimir(self):
		if self.topo == None:
			print("Pilha vazia")
		else:
			aux = self.topo 
			while(aux) :
				print(aux.dado)
				aux = aux.proximo
			print("Tamanho: " , self.tamanho)
	
	def desempilhar(self):
		if self.topo == None:
			print("Pilha vazia")
		else:
			self.topo = self.topo.proximo
			self.tamanho -= 1
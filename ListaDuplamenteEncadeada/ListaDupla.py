from No import No

class ListaDuplamenteEncadeada:
	def __init__(self):
		self.inicio = None
		self.fim = None
		self.tamanho = 0

	def inserir(self, valor):
		no = No(valor)
		if self.inicio :
			aux = self.inicio
			while(aux.proximo):
				aux = aux.proximo
			aux.proximo = no
			no.anterior = aux
		else: 
			self.inicio = no	
		self.fim = no
		self.tamanho += 1

	def imprimir(self):
		if  self.inicio == None:			
			print("lista vazia")
		else:
			aux = self.inicio
			while(aux):
				print(aux.dado)
				aux = aux.proximo
			print("Tamanho da lista: ", self.tamanho)

	def imprimirReverso(self):
		if self.fim == None:
			print("lista vazia")
		else:
			aux = self.fim
			while (aux) :
				print(aux.dado)
				aux = aux.anterior
			print("Tamanho da lista: ", self.tamanho)
			
	


	
	
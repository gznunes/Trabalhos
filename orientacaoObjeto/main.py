from desktop import Desktop
from notebook import Notebook

desktop = Desktop("Dell","Vermelho", "1000 reais", "700W")
notebook = Notebook("Lenovo", "Azul", "2000 reais", "7 horas")

print(desktop.modelo)

desktop.cadastrar()

notebook.cadastrar()

print(desktop.getInformacoes())


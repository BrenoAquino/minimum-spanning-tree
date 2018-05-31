'''

    Módulo executável.

'''

from sys import argv
from AlgoritmoMST import AlmMST
import ReadFileGrafo

if len(argv) > 1:
    PATH = argv[1]
else:
    PATH = str(input("Digite o caminho para o arquivo do grafo ou deixe em braco para o grafo padrão: "))
    if len(PATH) == 0:
        PATH = "./GrafoAnotado.txt"

grafo = ReadFileGrafo.grafoSimplesPonderado(PATH) # pylint: disable=C0103

# grafo.imprime()

mst = AlmMST() # pylint: disable=C0103

mst.gerarMST(grafo)

mst.imprime()

'''

    Módulo que inclui algoritmo não guloso de geração
    de MSTs, a seleção das arestas acontece de maneira
    aleatória.

'''

from random import randint
from PasseioGrafo import PasseioGrafo
from Grafo import GrafoTAD

# pylint: disable=C0103
class AlmMST:
    ''' Classe do algoritmo que gera a MST com uma abordagem não gulosa. '''

    def __init__(self):
        self.grafoArvore = GrafoTAD(0)
        self.arestas = []
        self.passeio = PasseioGrafo()

    def gerarMST(self, grafo):
        ''' Método que gera a MST a partir do grafo
            retornando as arestas da MST. '''
        self.grafoArvore = GrafoTAD(grafo.numVertices)
        self.arestas = grafo.arestas

        while len(self.arestas) > 0: #pylint: disable=C1801
            arestaIndex = randint(0, len(self.arestas) - 1)
            aresta = self.arestas[arestaIndex]
            self.arestas.remove(aresta)

            self.grafoArvore.insereAresta(aresta.v1, aresta.v2, aresta.peso)
            ciclo = self.passeio.geraCiclo(self.grafoArvore, aresta.v1)

            print("Aresta Inserida: (" +str(aresta.v1) + ", " + str(aresta.v2) + ")")

            if ciclo != None and len(ciclo) > 0: #pylint: disable=C1801
                # Verificar qual a aresta de menor custo do ciclo.
                arestaPesada = ciclo[0]
                for arestaCiclo in ciclo:
                    if arestaCiclo.peso > arestaPesada.peso:
                        arestaPesada = arestaCiclo

                arestaRemovida = self.grafoArvore.retiraAresta(arestaPesada.v1, arestaPesada.v2)

                print("Aresta Removida: (" +
                      str(arestaRemovida.v1) + ", " +
                      str(arestaRemovida.v2) + ")")

            print("Arvore: " + self.stringCiclo(self.grafoArvore.arestas))
            print("---")

        return self.grafoArvore.arestas

    def stringCiclo(self, ciclo): #pylint: disable=R0201
        ''' Método que retorna uma representação em string
            do ciclo gerado. '''
        if ciclo != None:
            toPrint = ""
            for aresta in ciclo:
                toPrint += "(" + str(aresta.v1) + ", " + str(aresta.v2) + ") "
            return toPrint
        return ""


    def imprime(self):
        ''' Método que imprime o ciclo encontrado
            junto de seu peso total. '''
        toPrint = ""
        totalPeso = 0
        for arestaArvore in self.grafoArvore.arestas:
            toPrint += "(" + str(arestaArvore.v1) + ", " + str(arestaArvore.v2) + ") "
            totalPeso += arestaArvore.peso

        toPrint += "- Peso Total: " + str(totalPeso)
        print(toPrint)
# pylint: enable=C0103

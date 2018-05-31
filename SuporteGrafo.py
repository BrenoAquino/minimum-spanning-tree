'''

    Módulo com classes auxiliares ao TAD Grafo.

'''

# pylint: disable=R0903
class Aresta:
    ''' Classe que representa uma aresta '''

    def __init__(self, v1, v2, peso):
        # pylint: disable=C0103
        self.v1 = v1
        self.v2 = v2
        self.peso = peso
        # pylint: enable=C0103

class Celula:
    ''' Classe que representa uma célula '''

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

# pylint: enable=R0903

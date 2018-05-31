'''

    Módulo que contém método para leitura de um arquivo txt
    descritivo de um grafo por matriz de adjacência.

'''

import re
from Grafo import GrafoTAD

# pylint: disable=C0103

def grafoSimplesPonderado(path):
    ''' Lê do arquivo em path um grafo simples sem peso nas arestas. '''

    fileGrafo = open(path, "r")

    numVertices = int(fileGrafo.readline())
    grafo = GrafoTAD(numVertices)

    # Criação de matriz NxN vazia.
    matriz = [[0 for x in range(numVertices)] for y in range(numVertices)]

    linhas = fileGrafo.readlines()
    for i in range(numVertices):
        linha = re.split(r'\s', linhas[i])
        for j in range(numVertices):
            try:
                if re.match(r'\s', linha[j]):
                    raise "Matriz incompleta!"
                matriz[i][j] = linha[j]
            except IndexError:
                raise "Matriz incompleta!"

    for i in range(numVertices):
        for j in range(numVertices):
            if matriz[i][j] != matriz[j][i]:
                raise "Grafo dirigido não suportado!"
            elif matriz[i][j] != "0" and matriz[i][j] != "inf":
                if not grafo.existeAresta(i, j):
                    grafo.insereAresta(i, j, int(matriz[i][j]))

    return grafo

# pylint: enable=C0103

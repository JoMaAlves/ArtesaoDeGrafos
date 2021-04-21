from prints import *
from graph import *
from platform import system
import os

#  𝓑𝓸𝓶 𝓭𝓲𝓪 𝓑𝓻𝓮𝓷𝓲𝓷𝓱𝓸, 𝓹𝓸𝓭𝓮𝓻𝓲𝓪𝓼 𝓲𝓷𝓹𝓾𝓽𝓪𝓻 𝓾𝓶 𝓰𝓻𝓪𝓯𝓸 𝓮𝓶 𝓷𝓸𝓼𝓼𝓸 𝓹𝓻𝓸𝓰𝓻𝓪𝓶𝓪? 

if(system() == "Windows"): 
    clear = "cls"
else:
    clear = "clear"

start, direc, valor = printStart(clear)

graph = graph(direc, valor)

while start:
    answer = printMenu()

    if ((answer == "0") or (answer.capitalize() == "Sair")):
        os.system(clear)
        break

    elif((answer == "1") or (answer.capitalize() == "Adicionar vertice")):
        graph.addNode()

    elif((answer == "2") or (answer.capitalize() == "Adicionar aresta")):
        graph.addEdge()

    elif((answer == "3") or (answer.capitalize() == "Imprimir grafo")):
        graph.printGraph()

    elif((answer == "4") or (answer.capitalize() == "Ordem do grafo")):
        graph.getOrder()

    elif((answer == "5") or (answer.capitalize() == "Tamanho do grafo")):
        graph.getSize()

    elif((answer == "6") or (answer.capitalize() == "Listar vertices adjacentes")):
        graph.adjacencyList()
        
    elif((answer == "7") or (answer.capitalize() == "Checar grau do vertice")):
        graph.getDegree()
    
    elif((answer == "8") or (answer.capitalize() == "Checar adjacencia")):
        graph.adjacencyCheck()

printThanks()
from menu import printMenu
from graph import *
from platform import system
import os

if(system() == "Windows"): 
    clear = "cls"
else:
    clear = "clear"

start, direc, valor = printMenu(0, clear)

graph = graph(direc, valor)

while start:
    answer = printMenu(1, clear)

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
    elif((answer == "6") or (answer.capitalize() == "Checar vertices adjacentes")):
        graph.adjacencyCheck()
    elif((answer == "7") or (answer.capitalize() == "Checar grau do vertice")):
        graph.getDegree()
    
    os.system(clear)
    

printMenu(2, clear)
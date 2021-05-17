from components.prints import *
from components.graph import *
from platform import system
import os

#  𝓑𝓸𝓶 𝓭𝓲𝓪 𝓑𝓻𝓮𝓷𝓲𝓷𝓱𝓸, 𝓹𝓸𝓭𝓮𝓻𝓲𝓪𝓼 𝓲𝓷𝓹𝓾𝓽𝓪𝓻 𝓾𝓶 𝓰𝓻𝓪𝓯𝓸 𝓮𝓶 𝓷𝓸𝓼𝓼𝓸 𝓹𝓻𝓸𝓰𝓻𝓪𝓶𝓪? 

if(system() == "Windows"): 
    clear = "cls"
else:
    clear = "clear"

# Prints the Capybara loading screen
animator(0.2, 3, clear)

# Gets the basic information for the software
start, direc, weight = printStart(clear)

# Creates the graph
graph = graph(direc, weight)

# Loop that maintains the software
while start:
    # Prints the Menu and gets the choice
    answer = printMenu()

    # Graph functions will be called according to the choice
    if ((answer == "0") or (answer.capitalize() == "Sair")):
        os.system(clear)
        break

    elif((answer == "1") or (answer.capitalize() == "Adicionar vertice")):
        graph.addNode()
        continue

    elif((answer == "2") or (answer.capitalize() == "Adicionar aresta")):
        graph.addEdge()
        continue

    elif((answer == "3") or (answer.capitalize() == "Imprimir grafo")):
        graph.printGraph()
        continue

    elif((answer == "4") or (answer.capitalize() == "Ordem do grafo")):
        graph.getOrder()
        continue

    elif((answer == "5") or (answer.capitalize() == "Tamanho do grafo")):
        graph.getSize()
        continue

    elif((answer == "6") or (answer.capitalize() == "Listar vertices adjacentes")):
        graph.vertexAdjacencyList()
        continue
        
    elif((answer == "7") or (answer.capitalize() == "Checar grau do vertice")):
        graph.getDegree()
        continue
    
    elif((answer == "8") or (answer.capitalize() == "Checar adjacencia")):
        graph.adjacencyCheck()
        continue

printThanks()
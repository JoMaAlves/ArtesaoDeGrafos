import math
import time
import os
from beautifultable import BeautifulTable

def printStart(clear):
    print("""
                         ___                  __   __  _             _
                        | _ )  ___   _ __     \ \ / / (_)  _ _    __| |  ___ 
                        | _ \ / -_) | '  \     \ V /  | | | ' \  / _` | | _ |
                        |___/ \___| |_|_|_|     \_/   |_| |_||_| \__,_| |___|
                                            __ _   ___ 
                                           / _` | | _ |
                                           \__,_| |___|
                             ___   _        _                         
                            / __| (_)  ___ | |_   ___   _ __    __ _  
                            \__ \ | | (_-< |  _| / -_) | '  \  / _` | 
                            |___/ |_| /__/  \__| \___| |_|_|_| \__,_| 
   _           _                                  _            ___                 __            
  /_\    _ _  | |_   ___   ___  __ _   ___     __| |  ___     / __|  _ _   __ _   / _|  ___   ___
 / _ \  | '_| |  _| / -_) (_-< / _` | / _ \   / _` | / -_)   | (_ | | '_| / _` | |  _| / _ \ (_-<
/_/ \_\ |_|    \__| \___| /__/ \__,_| \___/   \__,_| \___|    \___| |_|   \__,_| |_|   \___/ /__/
    """)

    print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo?                  |
                    |                                                          |
                    |                  [ 1 ] Sim   [ 2 ] Nao                   |
                    |                                                          |
                    +----------------------------------------------------------+
    """)

    while True:
        start = input("                             Resposta: ")
        if (start == "2") or (start.capitalize() == "Nao"):
            return 0, None, None
        elif ((start == "1") or (start.capitalize() == "Sim")):
            break
    
    os.system(clear)
        
    print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo:                  |
                    |                                                          |
                    |         [ 1 ] Direcionado   [ 2 ] Nao Direcionado        |
                    |                                                          |
                    +----------------------------------------------------------+
    """)

    answer1 = None
    while True:
        answer1 = input("                             Resposta: ")
        
        if ((answer1 == "1") or (answer1.capitalize() == "Direcionado")):
            answer1 = True
            break
        
        elif ((answer1 == "2") or (answer1.capitalize() == "Nao direcionado")):
            answer1 = False
            break

    os.system(clear)
        
    print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo:                  |
                    |                                                          |
                    |            [ 1 ] Valorado   [ 2 ] Nao Valorado           |
                    |                                                          |
                    +----------------------------------------------------------+
    """)

    answer2 = None
    while True:
        answer2 = input("                             Resposta: ")
        
        if ((answer2 == "1") or (answer2.capitalize() == "Valorado")):
            answer2 = True
            break
        
        elif ((answer2 == "2") or (answer2.capitalize() == "Nao valorado")):
            answer2 = False
            break

        
    os.system(clear)
    return 1, answer1, answer2

def printMenu():
    print("""
                                   __  __                     
                                  |  \/  |  ___   _ _    _  _ 
                                  | |\/| | / -_) | ' \  | || |
                +---------------- |_|  |_| \___| |_||_|  \_,_| ----------------+                      
                |                                                              |
                |   [ 1 ] Adicionar Vertice   [ 6 ] Listar Vertices Adjacentes |
                |   [ 2 ] Adicionar Aresta    [ 7 ] Checar Grau de Vertice     |
                |   [ 3 ] Imprimir Grafo      [ 8 ] Checar Adjacencia          |
                |   [ 4 ] Ordem do Grafo      [ 9 ] Calcular Menor Distacia    |
                |   [ 5 ] Tamanho do Grafo    [ 0 ] Sair                       |
                |                                                              |
                +--------------------------------------------------------------+
    """)

    return input("                             Resposta: ")

def printAddNode():
    print("""
                +--------------------------------------------------------------+                      
                |                                                              |
                |      Digite os valores dos vertices a serem adicionados:     |
                |                 - Separados por espaco                       |
                |                 - A quantidade que quiser                    |
                |                                                              |
                |                  Ex: '5 Nodo3 alpha @!3'                     |
                |                                                              |
                +--------------------------------------------------------------+
                       
                       Vertice(s):""", end=" ")

def printAddEdge():
    print("""
                +--------------------------------------------------------------+                      
                |                                                              |
                |            Digite os vertices a serem conectados:            |
                |                 - Separados por espaco                       |
                |                                                              |
                |                          Ex: 'ab c'                          |
                |                                                              |
                |         Deixe vazio e pressione < Enter > para voltar        |
                +--------------------------------------------------------------+
        
                        Vertices:""", end=" ")


def printValue(choice, value):
    size = len(str(value))
    
    print("\n")
        
    if(choice == "GetSize"):
        print(30*" " + "+------------- Tamanho ------------+")
    else:
        print(30*" " + "+-------------- Ordem -------------+")
    
    spaces = math.floor((34 - size)/2)
    if (size % 2 == 1):
        print(30*" " + "|" + (spaces + 1) * " " + f"{value}" + spaces * " " + "|")
    else:
        print(30*" " + "|" + spaces * " " + f"{value}" + spaces * " " + "|")

    print(30*" " + "+----------------------------------+")


def printDegree():
    print("""
                +--------------------------------------------------------------+
                |                                                              |
                |           Deseja visualizar o grau de que vertice?           |
                |                                                              |
                +--------------------------------------------------------------+
        
                        Digite o vertice:""", end=" ")


def printGetDegree(direc, value, value2 = None):
    size1 = len(str(value))
    size = size1

    if(direc):
        size2 = len(str(value2))
        size3 = len(str(value + value2))
        size = max(size, size2, size3)

    spaces = math.floor((40 - size)/2)

    print("\n")
    print(27*" " + "+------------ Grau Adjacencia -----------+")

    if(direc):
        print(27*" " + "|" + 40*" " + "|")

        if (size % 2 == 1):
            print(27*" " + "|" + (spaces - 8) * " " + "Entrada: " + f"{value2}" + spaces * " " + (size - size2) * " " + "|")
            print(27*" " + "|" + (spaces - 8) * " " + "  Saida: " + f"{value}" + spaces * " " + (size - size1) * " " + "|")
            print(27*" " + "|" + (spaces - 8) * " " + "  Total: " + f"{value + value2}" + spaces * " " + "|")
        else:
            print(27*" " + "|" + (spaces - 9) * " " + "Entrada: " +  f"{value2}" + spaces * " " + (size - size2) * " " + "|")
            print(27*" " + "|" + (spaces - 9) * " " + "  Saida: " + f"{value}" + spaces * " " + (size - size1) * " " + "|")
            print(27*" " + "|" + (spaces - 9) * " " + "  Total: " + f"{value + value2}" + spaces * " " + "|")

        print(27*" " + "|" + 40*" " + "|")
    else:
        if (size % 2 == 1):
            print(27*" " + "|" + (spaces + 1) * " " + f"{value}" + spaces * " " + "|")
        else:
            print(27*" " + "|" + spaces * " " + f"{value}" + spaces * " " + "|")

    print(27*" " + "+----------------------------------------+")

def printAdjListMenu():
    print("""
                   +--------------------------------------------------------+   
                   |                                                        |
                   |              Deseja visualizar a lista de              |
                   |               adjacencia de que vertice?               |
                   |                                                        |
                   +--------------------------------------------------------+
        
                            Digite o vertice:""", end=" ")


def printAdjList(direc, next, prev = None):

    size = len(next)
    spaces = math.floor((62 - size)/2)

    print("\n")
    print(16*" " + "+-------------------- Lista de Adjacencia ---------------------+")

    if(direc):
        if(len(prev) > len(next)):
            size = len(prev)
        
        print(16*" " + "|" + 62*" " + "|")
        
        if (size % 2 == 1):
            print(16*" " + "|" + (spaces - 8) * " " + "Entrada: " + prev + spaces * " " + (size - len(prev)) * " " + "|")
            print(16*" " + "|" + (spaces - 8) * " " + "  Saida: " + next + spaces * " " + (size - len(next)) * " " + "|")
        else:
            print(16*" " + "|" + (spaces - 9) * " " + "Entrada: " + prev + spaces * " " + (size - len(prev)) * " " + "|")
            print(16*" " + "|" + (spaces - 9) * " " + "  Saida: " + next + spaces * " " + (size - len(next)) * " " + "|")
        
        print(16*" " + "|" + 62*" " + "|")
    else:
        if (size % 2 == 1):
            print(16*" " + "|" + (spaces + 1) * " " + next + spaces * " " + "|")
        else:
            print(16*" " + "|" + spaces * " " + next + spaces * " " + "|")

    print(16*" " + "+--------------------------------------------------------------+")


def printAdjCheckMenu():
    print("""
                +--------------------------------------------------------------+                      
                |                                                              |
                |        Digite os vertices para checar sua adjacencia:        |
                |                    - Separados por espaco                    |
                |                                                              |
                |                          Ex: '12 5'                          |
                |                                                              |
                +--------------------------------------------------------------+
        
                         Vertices:""", end=" ")
def printAdjCheckResult(check):
    find = "nao"
    if(check):
        find = "sao"
    
    print(f"""
                              +----------------------------------+
                              |      Vertices {find} Adjacentes     |
                              +----------------------------------+              
    """)


def printGraphMenu():
    print("""
                +--------------------------------------------------------------+                      
                |                                                              |
                |            De que forma deseja imprimir seu grafo:           |
                |                                                              |
                |                  [ 1 ] Lista de Adjacencia                   |
                |                  [ 2 ] Matriz de Adjacencia                  |
                |                  [ 3 ] Lista de Arestas                      |
                |                                                              |
                |      Opcao < 3 > disponivel apenas com grafos valorados!     |
                +--------------------------------------------------------------+
        
                         Escolha:""", end=" ")

def printAdjacencyList(vertex, destinies):
    subtable = BeautifulTable(maxwidth=120)
    subtable2 = BeautifulTable(maxwidth=240)
    
    subtable.columns.append(vertex)

    for i in destinies:
        subtable2.rows.append(i)

    subtable.set_style(BeautifulTable.STYLE_BOX)
    subtable2.set_style(BeautifulTable.STYLE_BOX)

    parent_table = BeautifulTable(maxwidth=360)
    parent_table.columns.header = ["Vertice Origem", "Destinos"]
    parent_table.rows.append([subtable, subtable2])
    parent_table.columns.padding_left = 0
    parent_table.columns.padding_right = 0
    
    parent_table.set_style(BeautifulTable.STYLE_BOX)
    print(parent_table)

def printAdjacencyMatrix(vertex, destinies):
    table = BeautifulTable(maxwidth=360)
    
    table.columns.header = vertex
    
    for i in destinies:
        table.rows.append(i)
    
    table.rows.header = vertex
    table.set_style(BeautifulTable.STYLE_BOX)

    print(table)

def printListEdges(vertex,destinies):
    table = BeautifulTable(maxwidth=360)

    table.columns.header = ["Vértice de Saída","Vértice de Chegada"]

    for i in destinies:
        table.rows.append(i)

    table.rows.header = vertex
    table.set_style(BeautifulTable.STYLE_BOX)

    print(table)

def printDone():
    print("""
                              +----------------------------------+
                              |              Feito!              |
                              +----------------------------------+              
    """)

def printNotFound():
    print("""
                              +----------------------------------+
                              |     Vertice(s) nao encontrado    |
                              +----------------------------------+              
    """)

def printSameVertex():
    print("""
                       +------------------------------------------------+
                       |   Acao nao pode ser concluida: Mesmo Vertice   |
                       +------------------------------------------------+              
    """)

def printParalelEdge():
    print("""
                     +----------------------------------------------------+
                     |    Acao nao pode ser concluida: Aresta Paralela    |
                     +----------------------------------------------------+
    """)

def printDijkstraMenu():
    print("""
                           ___    _    _   _          _                
                          |   \  (_)  (_) | |__  ___ | |_   _ _   __ _ 
                          | |) | | |  | | | / / (_-< |  _| | '_| / _` |
                +-------- |___/  |_| _/ | |_\_\ /__/  \__| |_|   \__,_| -------+
                |                   |__/                                       |
                |                                                              |
                |     - Digite o vertice de origem e o vertice de destino      |
                |          para calcular a menor distancia entre eles          |
                |                                                              |
                |     - Digite apenas o vertice de origem para calcular a      |
                |           menor distancia entre ele e cada um dos            |
                |                     vertices existentes                      |
                |                                                              |
                |                      Ex: 'Nodo1 Nodo3'                       |
                |                                                              |
                +--------------------------------------------------------------+
                       
                       Vertice(s):""", end=" ")

def printThanks():
    print("""
                         ___    _            _                    _       
                        / _ \  | |__   _ _  (_)  __ _   __ _   __| |  ___ 
                       | (_) | | '_ \ | '_| | | / _` | / _` | / _` | | _ |
                        \___/  |_.__/ |_|   |_| \__, | \__,_| \__,_| |___|
                                                |___/                     
                                          _ __   ___   _ _ 
                                         | '_ \ / _ \ | '_|
                                         | .__/ \___/ |_|  
                                         |_|               
                     ___                _     _        _                     
                    | _ \  __ _   _ _  | |_  (_)  __  (_)  _ __   __ _   _ _ 
                    |  _/ / _` | | '_| |  _| | | / _| | | | '_ \ / _` | | '_|
                    |_|   \__,_| |_|    \__| |_| \__| |_| | .__/ \__,_| |_|  
                                                          |_|                
    """)


def animator (delay, repeat, clear):
    filesnames = ["../../public/capivara1.txt", "../../public/capivara2.txt", "../../public/capivara3.txt", "../../public/capivara2.txt", "../../public/capivara1.txt"]
    
    frames = []
    here = os.path.dirname(os.path.abspath(__file__))
    
    for name in filesnames:
        with open(os.path.join(here, name), "r", encoding="utf8") as f:
            frames.append(f.readlines())
    
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system(clear)
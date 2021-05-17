from components.prints import *

class vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.prevEdges = []
        self.nextEdges = []
        #next aponta 
        #prev é apontado.

    # Adds an edge to the edges list if the graph is not directed
    def addEdge(self, edge):
        self.edges.append(edge)

    # Adds an edge to the nextEdges list if it is a  directed graph
    def addNext(self, next):
        self.nextEdges.append(next)

    # Adds an edge to the prevEdges list if it is a  directed graph
    def addPrevious(self, prev):
        self.prevEdges.append(prev)

    # Checks if there is a connection between the vertex already
    def checkEdges(self, vertex, direc, weight):
        if(direc):
            for i in self.nextEdges:
                if(weight):
                    if(i[0] == vertex):
                        return True
                else:
                    if(i == vertex):
                        return True
            
            for i in self.prevEdges:
                if(weight):
                    if(i[0] == vertex):
                        return True
                else:
                    if(i == vertex):
                        return True
        
        else:
            for i in self.edges:
                if(weight):
                    if(i[0] == vertex):
                        return True
                else:
                    if(i == vertex):
                        return True
        
        return False

    # Gets the list of Adjacent Edges and place it into a string
    def listAdjacents(self, direc, weight):
        if(direc):
            next = ""
            prev = ""

            if(weight):
                for i in self.nextEdges:
                    next += str(i[0].value) + " "

                for i in self.prevEdges:
                    prev+=str(i[0].value) + " "
            else:
                for i in self.nextEdges:
                    next += str(i.value) + " "

                for i in self.prevEdges:
                    prev+=str(i.value) + " "
    
            printAdjList(direc, next.strip(), prev.strip())

        else:
            all = ""
            
            if(weight):
                for i in self.edges:
                    all +=str(i[0].value) + " "
            else:
                for i in self.edges:
                    all +=str(i.value) + " "

            printAdjList(direc, all.strip())

    # Check if two vertex are adjacent
    def adjacencyCheck(self, node, direc, weight):
        
        check = False
        if(direc):
            if(weight):
                for i in self.nextEdges:
                    if(node == i[0].value):
                        check = True
                
                for i in self.prevEdges:
                    if(node == i[0].value):
                        check = True
            else:
                for i in self.nextEdges:
                    if(node == i.value):
                        check = True
                
                for i in self.prevEdges:
                    if(node == i.value):
                        check = True
        else:
            if(weight):
                for i in self.edges:
                    if(node == i[0].value):
                        check = True
            else:
                for i in self.edges:
                    if(node == i.value):
                        check = True
            
        return check

    # Gets the degree of the vertex
    def getDegreeEdges(self,direc):
        if(direc):
            return len(self.nextEdges), len(self.prevEdges)
        else:
            return len(self.edges), None
    
    
    def getValuesList(self,direc, valor):
        lista_edges = []

        if(direc):
            for i in self.nextEdges:
                if(valor):
                    lista_edges.append(i[0].value)
                else:
                    lista_edges.append(i.value)

        else:
            for i in self.edges:
                if(valor):
                    lista_edges.append(i[0].value)
                else:
                    lista_edges.append(i.value)
        
        return lista_edges, len(lista_edges)

    def getMatrixAdj(self, direc, valor,list_elements):
        lista_aux_edges = []
        lista_final_edges = []
        if(direc):
            for i in self.nextEdges:
                if(valor):
                    lista_aux_edges.append(i[0])
                else:
                    lista_aux_edges.append(i)
        else:
            for i in self.edges:
                if(valor):
                    lista_aux_edges.append(i[0])
                else:
                    lista_aux_edges.append(i)
        
        for i in list_elements:
            if i in lista_aux_edges:
                lista_final_edges.append(1)
            else:
                lista_final_edges.append(0)
                

        return lista_final_edges
class graph:
    def __init__(self, direc, valor):
        self.nodeList = []
        self.direc = direc
        self.valor = valor
        self.order = 0
        self.size = 0

    def addNode(self):
        node = vertex(input("Digite o nome do seu Vertice: "))
        self.nodeList.append(node)
        self.order += 1

    def addEdge(self, node):
        if self.valor == 1:
            #add edge-> self.adj[grafo1].add(grafo2)
            if self.direc == 2:
                #//add node too-> self.adj[grafo2].add(grafo1)
                print("")
        else:
            #add edge
            if self.direc == 2:
                print("")
        self.size += 1
        return 0

    def printGraph(self):
        return 0
    
    def getOrder(self):
        return self.order
    
    def getSize(self):
        return self.size
    
    def getDegree(self, ):
        return 0
    
    def adjacencyCheck(self, graph1, graph2):
        return 0

class vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.degree = 0 
    
    def addNext(self, next):
        return 0
class edge:
    def __init__(self, value=None, mainNode=None, nextNode=None):
        self.value = value
        self.mainNode = mainNode
        self.nextNode = nextNode
    
    def setValue(self,value):
        self.value = value

    def setPrevNode(self, value):
        self.mainNode = value

    def setNextNode(self, value):
        self.nextNode = value
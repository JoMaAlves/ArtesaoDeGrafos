class graph:
    def __init__(self, direc, valor):
        self.nodeList = []
        self.direc = direc
        self.valor = valor
        self.order = 0
        self.size = 0

    def addNode(self):
        node = vertex(input())

    def printGraph(self):
        return 0
    
    def getOrder(self):
        return 0
    
    def getSize(self):
        return 0
    
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
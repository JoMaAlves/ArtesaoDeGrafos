from prints import *
from vertex import vertex

class graph:
    def __init__(self, direc, valor):
        self.nodeList = []
        self.direc = direc
        self.valor = valor
        self.size = 0

    def addNode(self):

        printAddNode()
        nodes = input()
        node_aux = nodes.strip().split(' ')
         
        for i in node_aux:
            check = False
            for j in self.nodeList:
                if(i == j.value):
                    check = True

            if(not check):
                self.nodeList.append(vertex(i))
        
        printDone()

    # Creates Edges over a loop
    def addEdge(self):
        while 1:
            printAddEdge()
            nodes = input()

            # Breaks creation if there is no input
            if(nodes == ""):
                printDone()
                break

            nodes = nodes.strip().split(" ")

            # Checks if there were more then 1 vertex and corrects if not
            if(len(nodes) == 1):
                sec = ""
                while sec == "":
                    print(" " * 24,end="")
                    sec = input("Digite o segundo vertice: ")

                nodes.append(sec)

            # Checks if it is the same vertex
            if(nodes[0] == nodes[1]):
                printSameVertex()
                continue

            # Checks if both vertex exist and connect them with the node variables
            check = [False, False]
            node1 = None
            node2 = None
            for i in range(len(nodes)):
                if(i == 1 and check[0] == False):
                    break
                for j in self.nodeList:
                    if(nodes[i] == j.value):
                        check[i] = True
                        if(i):
                            node2 = j
                        else:
                            node1 = j      
                        break
            
            # Checks if both vertex were found
            if(check[0] == False or check[1]== False):
                printNotFound()
                continue
            
            # Check if it is a paralel conection
            if(node1.checkEdges(node2, self.direc, self.valor)):
                printParalelEdge()
                continue
            
            # Adds the edge into the nodes edge lists according to weight and direction
            if(self.valor):
                # Gets the edge's weight
                print(" " * 24,end="")
                weight = int(input("Digite o valor da aresta: "))

                # A tuple is being used if there is a weight for the edge (vertex, weight)
                if(self.direc):    
                    node1.addNext( (node2, weight) )
                    node2.addPrevious( (node1, weight) )
                else:
                    node1.addEdge( (node2, weight) )
                    node2.addEdge( (node1, weight) )

            else:
                if(self.direc):    
                    node1.addNext( node2 )
                    node2.addPrevious( node1 )
                else:
                    node1.addEdge( node2 )
                    node2.addEdge( node1 )

            self.size += 1

        printDone()


    def printGraph(self):
        vertex, destinies = self.getMatrix()
        #v, d = self.getAdj()
        printAdjacencyMatrix(vertex, destinies)
        #printAdjacencyMatrix(v, d)
    
    # Gets the graph order
    def getOrder(self):
        printValue( "GetOrder", len(self.nodeList) )
    
    # Gets the graph size
    def getSize(self):
        printValue( "GetSize", self.size )
    
    # Gets the graph degree
    def getDegree(self):
        printDegree()
        vert= input().strip()

        # Get the degree of a vertex call its method getDegreeEdges()
        found = False
        answer, answer2 = None, None
        for i in self.nodeList:
            if(i.value == vert):
                answer, answer2 = i.getDegreeEdges(self.direc)
                found = True
                break
        
        # Breaks if the vertex was not found
        if(not found):
            printNotFound()
            return 1

        # Checks if the graph is directed not
        if(self.direc):
            printGetDegree( answer, answer2 )
        else:
            printGetDegree( answer )
    
    # Gets the list of adjacency of a vertex
    def adjacencyList(self):
        printAdjListMenu()
        check = input().strip()
        
        # Search for the node and gets its list using its method listAdjacents()
        found = False
        for i in self.nodeList:
            if(i.value == check):
                i.listAdjacents(self.direc)
                found = True
                break
        
        # If not found, breaks
        if(not found):
            printNotFound()
            return 1

    # Checks the adjacency between two vertex
    def adjacencyCheck(self):
        printAdjCheckMenu()
        vertex = input().strip().split(" ")
        
        # Looks over one vertex for the other
        found = False
        for i in self.nodeList:
            if(i.value == vertex[0]):
                i.adjacencyCheck(vertex[1],self.direc)
                break
        
        # Breaks if not found
        if(not found):
            printNotFound()
            return 1
    

    def getMatrix(self):
        list_vertex = []
        list_edges = []
        max_size = 0
        for i in self.nodeList:
            list_vertex.append(i.value)
            list_aux, size = i.getValuesMatrix(self.direc, self.valor)
            list_edges.append(list_aux)
            if(size > max_size):
                max_size = size

        for i in list_edges:
            while(len(i) < max_size):
                i.append("")
        
        return list_vertex,list_edges

    def getAdj(self):
        list_vertex = []
        list_edges = []
        max_size = 0
        for i in self.nodeList:
            list_vertex.append(i.value)
            list_aux, size = i.getMatrixAdj(self.direc, self.valor,self.nodeList)
            list_edges.append(list_aux)
            if(size > max_size):
                max_size = size

        for i in list_edges:
            while(len(i) < max_size):
                i.append("")
            
        return list_vertex,list_edges
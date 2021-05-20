from components.prints import *
from components.vertex import vertex

class graph:
    def __init__(self, direc, weight):
        self.nodeList = []
        self.edgeList = []
        self.direc = direc
        self.weight = weight
        self.size = 0

    # Adds a vertex
    def addNode(self):

        printAddNode()
        nodes = input()
        node_aux = nodes.strip().split(' ')

        if(nodes.strip() == ""):
            return 1
        
        # Check if the nodes exist
        newNodes = []
        for i in node_aux:
            check = False
            for j in self.nodeList:
                if(i == j.value):
                    check = True

            if(not check):
                newNodes.append(i)

        if(len(self.nodeList)):
            for i in self.nodeList:
                i.addNewPaths(newNodes)

        for i in newNodes:
            self.nodeList.append(vertex(i,dict.fromkeys(self.getNodes() + newNodes)))

        printDone()

    # Creates Edges over a loop
    def addEdge(self):
        while 1:
            printAddEdge()
            nodes = input()

            # Breaks creation if there is no input
            if(nodes.strip() == ""):
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
            if(not check[0] or not check[1]):
                printNotFound()
                continue
            
            # Check if it is a paralel conection
            if(node1.checkEdges(node2, self.direc, self.weight)):
                printParalelEdge()
                continue
            
            # Adds the edge into the nodes edge lists according to weight and direction
            if(self.weight):
                # Gets the edge's weight
                while True:
                    try:
                        print(" " * 24,end="")
                        new_weight = int(input("Digite o peso da aresta: "))
                        break
                    except:
                        continue

                self.edgeList.append( (new_weight, node1.value, node2.value) )

                # A tuple is being used if there is a weight for the edge (vertex, weight)
                if(self.direc):    
                    node1.addNext( (node2, new_weight) )
                    node2.addPrevious( (node1, new_weight) )
                else:
                    node1.addEdge( (node2, new_weight) )
                    node2.addEdge( (node1, new_weight) )

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
        printGraphMenu()
        answer = input().strip()

        if(answer == "1" or answer.capitalize() == "Lista de adjacencia"):
            vertex, destinies= self.getGraph(1)
            printAdjacencyList(vertex, destinies)

        elif(answer == "2" or answer.capitalize() == "Matriz de adjacencia"):
            vertex, binary = self.getGraph(2)
            printAdjacencyMatrix(vertex, binary)
        
        elif(answer == "3" or answer.capitalize() == "Lista de arestas"):
            edges, destinies = self.returnEdges()
            printListEdges(edges, destinies)
    
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
            printGetDegree( self.direc, answer, answer2 )
        else:
            printGetDegree( self.direc, answer )
    
    # Gets the list of adjacency of a vertex
    def vertexAdjacencyList(self):
        printAdjListMenu()
        check = input().strip()
        
        # Search for the node and gets its list using its method listAdjacents()
        found = False
        for i in self.nodeList:
            if(i.value == check):
                i.listAdjacents(self.direc, self.weight)
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
        
        # Looks over a vertex, for the other one
        found = False
        for i in self.nodeList:
            if(i.value == vertex[0]):
                result = i.adjacencyCheck(vertex[1], self.direc, self.weight)
                found = True
                break
        
        # Breaks if not found
        if(not found):
            printNotFound()
            return 1

        printAdjCheckResult(result)
    
    def getGraph(self, choice):
        list_values = []
        list_table = []

        max_size = 0
        for i in self.nodeList:
            list_values.append(i.value)

            if(choice == 1):
                list_aux, size = i.getValuesList(self.direc, self.weight)
                if(size > max_size):
                    max_size = size
            elif(choice == 2):
                list_aux = i.getMatrixAdj(self.direc, self.weight,self.nodeList)

            list_table.append( list_aux)

        if(choice == 1):
            for i in list_table:
                while(len(i) < max_size):
                    i.append("")


        return list_values,list_table

    def returnEdges(self):
        list_weight = []
        list_destinies = []
        for i in self.edgeList:
            list_weight.append(str(i[0]))
            list_destinies.append( (i[1],i[2]) )

        
        return list_weight,list_destinies
    
    def dijkstraAlgorithm(self):
        if(not self.direc or not self.weight):
            return 1

        printDijkstraMenu()
        nodes = input()

        # Breaks creation if there is no input
        if(nodes.strip() == ""):
            return 1

        nodes = nodes.strip().split(" ")
        
        # Checks if both vertex were found
        result = None
        if(len(nodes) == 2):
            check = ( self.checkNodeExists(nodes[0]), self.checkNodeExists(nodes[1]) )
            if(check[0][0] and check[1][0]):
                return 0
            else:
                printNotFound()
                return 1
        else:
            check = self.checkNodeExists(nodes[0])
            if(check[0]):
                return 0
            else:
                printNotFound()
                return 1

    def checkNodeExists(self, node):
        for i in self.nodeList:
            if(node == i.value):
                return (True, i)
        
        return (False, None)

    def getNodes(self):
        nodes = []
        for i in self.nodeList:
            nodes.append(i.value)
        
        return nodes
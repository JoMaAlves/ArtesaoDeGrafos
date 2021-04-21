from prints import *

class graph:
    def __init__(self, direc, valor):
        self.nodeList = []
        self.direc = direc
        self.valor = valor
        self.size = 0

    # === DONE ===
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


    def addEdge(self):
        while 1:
            #Adds an Edge
            printAddEdge()
            nodes = input()

            if(nodes == ""):
                break

            nodes = nodes.strip().split(" ")

            #Checks if there were more then 1 vertex and corrects if not
            if(len(nodes) == 1):
                sec = ""
                while sec == "":
                    print(" " * 20,end="")
                    sec = input("Digite o segundo vertice: ")

                nodes.append(sec)

            if(nodes[0] == nodes[1]):
                print("Nao eh possivel ligar o nodo a ele mesmo")
                continue

            #Checks if both vertex exist
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

            if(check[0] == False or check[1]== False):
                printNotFound()
                continue

            if(self.valor):
                print(" " * 20,end="")
                weight = input("Digite o valor da aresta: ")

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
            #break

        printDone()


    def printGraph(self):
        for i in self.nodeList:
            print(i.value, end="-")
    
    # === DONE ===
    def getOrder(self):
        printValue( "GetOrder", len(self.nodeList) )
    
    # === DONE ===
    def getSize(self):
        printValue( "GetSize", self.size )
    

    def getDegree(self):
        printDegree()
        vert= input().strip()
        found = False
        answer, answer2 = None, None
        for i in self.nodeList:
            if(i.value == vert):
                answer, answer2 = i.getDegreeEdges(self.direc)
                found = True
                break

        if(not found):
            printNotFound()
            return 1

        if(self.direc):
            printGetDegree( answer, answer2 )
        else:
            printGetDegree( answer )
    

    def adjacencyList(self):
        printAdjListMenu()
        check = input().strip()
        
        found = False
        for i in self.nodeList:
            if(i.value == check):
                i.listAdjacents(self.direc)
                found = True
                break
        
        if(not found):
            printNotFound()
            return 1


    def adjacencyCheck(self):
        printAdjCheckMenu()
        vertex = input().strip().split(" ")
        
        found = False
        for i in self.nodeList:
            if(i.value == vertex[0]):
                i.adjacencyCheck(vertex[1],self.direc)
                break
        
        if(not found):
            printNotFound()
            return 1
    

    def getMatrix(self):
        '''
        from beautifultable import BeautifulTable
        table = BeautifulTable()
        matrix = []
        lista_values = []
        for i in self.nodeList:
            list_aux =i.getValuesMatrix(self.nodeList,i.value)
            matrix.append(list_aux)
            lista_values.append(i.value)
        
        table.column_headers =lista_values
        for i in matrix:
            table.append_row(i)
        
        print(table)

        #df_matrix=  pd.DataFrame((matrix),columns=self.nodeList)
        #show(df_matrix)
        '''

class vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.prevEdges = []
        self.nextEdges = []
        #next aponta 
        #prev é apontado.


    def addEdge(self, edge):
        self.edges.append(edge)


    def addNext(self, next):
        self.nextEdges.append(next)


    def addPrevious(self, prev):
        self.prevEdges.append(prev)


    def listAdjacents(self,direc):
        if(direc):
            next = ""
            prev = ""

            for i in self.nextEdges:
                next += str(i.value) + " "

            for i in self.prevEdges:
                prev+=str(i.value) + " "
    
            printAdjList(direc, next.strip(), prev.strip())

        else:
            all = ""

            for i in self.edges:
                all +=str(i.value) + " "

            printAdjList(direc, all.strip())

    def adjacencyCheck(self, node, direc):
        
        check = False
        if(direc):
            for i in self.nextEdges:
                if(node == i.value):
                    check = True
        else:
            for i in self.edges:
                if(node == i.value):
                    check = True
            
        
        if(check):
            print("Os vértices são adjacentes")
        else:
            print("Os vértices não são adjacentes")


    def getDegreeEdges(self,direc):
        if(direc):
            return len(self.nextEdges), len(self.prevEdges)
        else:
            return len(self.edges)
    
    def getValuesMatrix(self,list_elements,value_select):
        '''

        lista=[]
        lista.append(value_select)
        for i in list_elements:
            if(i.value in self.nextEdges):
                lista.append(1)
            else:
                lista.append(0)
        
        return lista



        '''

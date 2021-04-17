from menu import printMenu


class graph:
    def __init__(self, direc, valor):
        self.nodeList = []
        self.direc = direc
        self.valor = valor
        self.size = 0
        self.lista_arestas=[]

    def addNode(self):

        print("""
                        Digite os valores dos vertices a serem adicionados:
                           - Separados por espaco
                           - A quantidade que quiser

                        Ex: '5 Nodo3 alpha @!3'
            """)
    
        print(" " * 20,end="")
        nodes = input("Resposta: ")
        node_aux = nodes.strip().split(' ')
        
         
        for i in node_aux:
            check = False
            for j in self.nodeList:
                if(i == j.value):
                    check = True
            if(not check):
                self.nodeList.append(vertex(i))


    def addEdge(self):
        weight = None
        while 1:
            #Adds an Edge
            print("""
                        Digite os vertices a serem conectados:
                        Ex: '12 5'
                        ( Separados por Espaco )
            """)
            print(" " * 20,end="")
            answer = input("Resposta: ")
            nodes = answer.split(' ')

            #Checks if there were more then 1 vertex and corrects if not
            if(len(nodes) == 1):
                sec = ""
                while sec == "":
                    print("=" * 20,end="")
                    sec = input("Digite o segundo vertice: ")
                
                nodes.append(sec)

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
                print(" " * 20,end="")
                print("Algum vertice inexistente!")
                continue

            if(self.valor):
                print("=" * 20,end="")
                weight = input("Digite o valor da aresta: ")
                node1.addNext( (node2, weight) )
                node2.addPrevious( (node1, weight) )
            else:
                node1.addNext( (node2) )
                node2.addPrevious( (node1) )
            

            self.size += 1

    def printGraph(self):
        for i in self.nodeList:
            print(i.value, end="-")
    
    def getOrder(self):
        print(len(self.nodeList))
    
    def getSize(self):
        print(self.size)
    
    def getDegree(self, ):
        return 0
    
    def adjacencyCheck(self):
        return 0

class vertex:
    def __init__(self, value):
        self.value = value
        self.degree = 0
        self.prevEdges = []
        self.nextEdges = []
        #next aponta 
        #prev é apontado.

    def addNext(self, next):
        self.nextEdges.append(next)
        print(self.nextEdges)

    def addPrevious(self, prev):
        self.prevEdges.append(prev)
        print(self.prevEdges)
        

         
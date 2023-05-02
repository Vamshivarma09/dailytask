# ipt = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
# n = 6
# mg = []
# for i in range(6):
#     temp=[]
#     for j in range(6):
#         temp.append(0)
#     mg.append(temp)

# for (u,v) in ipt:
#     mg[u][v] = 1
#     mg[v][u] = 1

# for item in mg:
#     print(item)

# adjacency matrix for 
# undirected graph

class Graph:
    def __init__(self, numOfNodes):
        self.numOfNodes = numOfNodes
        # self.adjMatrix = [[0] * numOfNodes for i in range(numOfNodes)]
        self.adjMatrix = []
        for i in range(numOfNodes):
            # print(i)
            row = [0]*numOfNodes
            self.adjMatrix.append(row)

    def addEdge(self, value1,value2):
        self.adjMatrix[value1][value2] = 1
        self.adjMatrix[value2][value1] = 1

    def display(self):
        for row in self.adjMatrix:
            print(row)

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,3)

g.display()
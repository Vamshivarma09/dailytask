class Graph:
    def __init__(self,noofnodes):
        self.noofnodes=noofnodes
        self.adj_list = {}

    def add_edge(self, x, y):
        if x not in self.adj_list:
            self.adj_list[x] = []

        self.adj_list[x].append(y)

        if y not in self.adj_list:
            self.adj_list[y] = []
            
        self.adj_list[y].append(x)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print(g.adj_list)  

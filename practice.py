# class Graph:
#     def __init__(self, num_vertices):
#         self.num_vertices = num_vertices
#         self.adj_list = {i: [] for i in range(num_vertices)}

#     def add_edge(self, x, y):
#         self.adj_list[x].append(y)
#         self.adj_list[y].append(x)

#     def print_adj_list(self):
#         for vertex in self.adj_list:
#             print(f"Node {vertex}: {self.adj_list[vertex]}")

# # Create a graph with 4 nodes
# graph = Graph(4)

# # Add edges to the graph
# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(1, 3)
# graph.add_edge(2, 3)

# # Print the adjacency list
# graph.print_adj_list()

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {}

        # Initialize adjacency list with empty lists for each vertex
        for i in range(num_vertices):
            self.adj_list[i] = []

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def print_adj_list(self):
        for vertex in self.adj_list:
            print(f"Node {vertex}: {self.adj_list[vertex]}")

# Create a graph with 4 nodes
graph = Graph(5)

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)

# Print the adjacency list
graph.print_adj_list()

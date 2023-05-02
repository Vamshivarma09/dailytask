graph = {
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A"],
    "D":["B"],
    "E":["C","D"],
}

start = "A"

visited = set()

def dfs(graph,start):  
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor)

dfs(graph, start)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # for undirected graph

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbour in graph.graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbour in graph.graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Graph:")
g.print_graph()

print("\nDFS traversal starting from 0:")
dfs(g, 0)

print("\n\nBFS traversal starting from 0:")
bfs(g, 0)

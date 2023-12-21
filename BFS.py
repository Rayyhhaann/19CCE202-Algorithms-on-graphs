from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def bfs(self, start_vertex):
        visited = set()
        visited.add(start_vertex)
        queue = deque([start_vertex])
        while queue:
            current_vertex = queue.popleft()
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

# Create a different graph
new_graph = Graph()
new_graph.add_vertex("X")
new_graph.add_vertex("Y")
new_graph.add_vertex("Z")
new_graph.add_vertex("W")
new_graph.add_vertex("K")
new_graph.add_edge("X", "Y")
new_graph.add_edge("X", "Z")
new_graph.add_edge("Y", "Z")
new_graph.add_edge("Y", "W")
new_graph.add_edge("Z", "K")
new_graph.add_edge("W", "K")

# Visualize the different graph using NetworkX and Matplotlib
G = nx.Graph()
for vertex, neighbors in new_graph.adjacency_list.items():
    G.add_node(vertex)
    for neighbor in neighbors:
        G.add_edge(vertex, neighbor)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', arrowsize=15, node_size=700, node_color='lightblue', font_size=10)

plt.title("Graph Visualization")
plt.show()
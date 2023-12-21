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

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        traversal_path = []  # Store the traversal path
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                traversal_path.append(current_vertex)
                visited.add(current_vertex)

            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)

        return traversal_path

# Create a different graph
new_graph = Graph()
new_graph.add_vertex("X")
new_graph.add_vertex("Y")
new_graph.add_vertex("Z")
new_graph.add_vertex("W")
new_graph.add_vertex("K")
new_graph.add_edge("X", "Y")
new_graph.add_edge("X", "Z")
new_graph.add_edge("Y", "W")
new_graph.add_edge("Z", "W")
new_graph.add_edge("Z", "K")

# Print the graph structure
print("Graph Structure:")
new_graph.print_graph()
dfs_path = new_graph.dfs("X")
print("\nDFS Process:")
for vertex in dfs_path:
    print(vertex)
G = nx.Graph()
for vertex, neighbors in new_graph.adjacency_list.items():
    G.add_node(vertex)
    for neighbor in neighbors:
        G.add_edge(vertex, neighbor)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', arrowsize=15, node_size=700, node_color='lightblue', font_size=10)
plt.title("Graph Visualization")
plt.show()
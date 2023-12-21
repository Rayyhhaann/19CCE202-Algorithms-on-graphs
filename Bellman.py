import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.nodes = set()

    def add_edge(self, s, d, w):
        if s not in self.graph:
            self.graph[s] = []
        self.graph[s].append((d, w))
        self.nodes.update([s, d])

    def addNode(self, value):
        self.nodes.add(value)

    def visualize_graph(self):
        G = nx.DiGraph()
        for s in self.graph:
            for d, w in self.graph[s]:
                G.add_edge(s, d, weight=w)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=10)
        edge_labels = {(s, d): w for s in self.graph for d, w in self.graph[s]}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def bellmanFord(self, src):
        distances = {node: float("Inf") for node in self.nodes}
        distances[src] = 0

        for _ in range(self.V - 1):
            for s in self.graph:
                for d, w in self.graph[s]:
                    if distances[s] != float("Inf") and distances[s] + w < distances[d]:
                        distances[d] = distances[s] + w

        for s in self.graph:
            for d, w in self.graph[s]:
                if distances[s] != float("Inf") and distances[s] + w < distances[d]:
                    print("Graph contains a negative cycle")
                    return

        self.print_solution(distances)

    def print_solution(self, distances):
        print("\nVertex Distance from Source:")
        for node, distance in distances.items():
            print(f"{node}: {distance}" if distance != float("Inf") else f"{node}: ∞")

# Example usage with a new graph
g = Graph(6)
g.addNode("X")
g.addNode("Y")
g.addNode("Z")
g.addNode("W")
g.addNode("K")
g.addNode("L")

g.add_edge("X", "Y", 3)
g.add_edge("X", "Z", 7)
g.add_edge("Y", "Z", 2)
g.add_edge("Y", "W", 5)
g.add_edge("Z", "K", 4)
g.add_edge("W", "L", 6)
g.add_edge("W", "M", 1)
g.add_edge("K", "L", 8)
g.add_edge("L", "M", 9)

# Visualize the new graph
print("Graph Visualization:")
g.visualize_graph()

# Perform Bellman-Ford algorithm
print("\nBellman-Ford Algorithm:")
g.bellmanFord("X")
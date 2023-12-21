from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.node_indices = {}  # Map nodes to integers for indexing
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        if value not in self.node_indices:
            index = len(self.node_indices)
            self.node_indices[value] = index
            self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

    def visualize(self):
        G = nx.DiGraph()
        for node, index in self.node_indices.items():
            G.add_node(index, label=node)
        for fromNode, neighbors in self.edges.items():
            for toNode in neighbors:
                G.add_edge(self.node_indices[fromNode], self.node_indices[toNode], weight=self.distances[(fromNode, toNode)])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', arrowsize=15, node_size=700, node_color='lightblue', font_size=10)
        edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

    def floyd_warshall(self):
        num_nodes = len(self.nodes)
        distance_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]

        for node, index in self.node_indices.items():
            distance_matrix[index][index] = 0
            for neighbor in self.edges[node]:
                neighbor_index = self.node_indices[neighbor]
                distance_matrix[index][neighbor_index] = self.distances[(node, neighbor)]

        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    distance_matrix[i][j] = min(
                        distance_matrix[i][j],
                        distance_matrix[i][k] + distance_matrix[k][j]
                    )

        return distance_matrix


# Create a different graph
customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "D", 4)
customGraph.addEdge("C", "E", 7)
customGraph.addEdge("D", "E", 8)

# Visualize the different graph
print("Graph Visualization:")
customGraph.visualize()

# Run Floyd's algorithm
result_matrix = customGraph.floyd_warshall()

# Display the result matrix
print("\nFloyd's Algorithm Result:")
for row in result_matrix:
    print(row)
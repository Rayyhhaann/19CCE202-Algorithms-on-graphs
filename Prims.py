import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []

    def printSolution(self):
        print("Minimum Spanning Tree (MST):")
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def primsAlgo(self):
        visited = [0] * self.vertexNum
        edgeNum = 0
        visited[0] = True

        while edgeNum < self.vertexNum - 1:
            min_weight = sys.maxsize
            s, d = 0, 0

            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if not visited[j] and self.edges[i][j] and min_weight > self.edges[i][j]:
                            min_weight = self.edges[i][j]
                            s, d = i, j

            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1

            print(f"Selected edge: {self.nodes[s]} - {self.nodes[d]} ({self.edges[s][d]})")
            print(f"Visited nodes: {self.get_visited_nodes(visited)}")

        self.printSolution()
        self.plot_graph()

    def get_visited_nodes(self, visited):
        return [self.nodes[i] for i in range(self.vertexNum) if visited[i]]

    def plot_graph(self):
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node)
        for s, d, w in self.MST:
            G.add_edge(s, d, weight=w)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', arrowsize=15, node_size=700, node_color='lightblue', font_size=10)
        edge_labels = {(s, d): w for s, d, w in self.MST}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph Visualization")
        plt.show()


different_edges = [
    [0, 2, 4, 0, 0],
    [2, 0, 1, 5, 0],
    [4, 1, 0, 3, 6],
    [0, 5, 3, 0, 8],
    [0, 0, 6, 8, 0]
]

different_nodes = ["X", "Y", "Z", "W", "K"]
different_g = Graph(5, different_edges, different_nodes)
different_g.primsAlgo()
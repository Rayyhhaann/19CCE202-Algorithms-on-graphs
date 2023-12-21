import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        print("Minimum Spanning Tree (MST):")
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])

        print("Edges sorted by weight:")
        for edge in self.graph:
            print(f"{edge[0]} - {edge[1]}: {edge[2]}")

        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)

            print(f"Checking edge: {s} - {d} ({w})")

            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
                print(f"Selected edge: {s} - {d} ({w}), Added to MST")
                print(f"Sets after adding edge: {ds.get_sets()}")

        self.printSolution(s, d, w)
        self.plot_graph()

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


class DisjointSet:
    def __init__(self, nodes):
        self.parent = {}
        for node in nodes:
            self.parent[node] = node

    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        self.parent[y_set] = x_set

    def get_sets(self):
        sets = {}
        for node in self.parent:
            root = self.find(node)
            if root in sets:
                sets[root].append(node)
            else:
                sets[root] = [node]
        return sets


# Create a new graph
new_g = Graph(7)
new_g.addNode("A")
new_g.addNode("B")
new_g.addNode("C")
new_g.addNode("D")
new_g.addNode("E")
new_g.addNode("F")
new_g.addNode("G")

new_g.addEdge("A", "B", 3)
new_g.addEdge("A", "C", 5)
new_g.addEdge("B", "C", 1)
new_g.addEdge("B", "D", 6)
new_g.addEdge("C", "D", 2)
new_g.addEdge("C", "E", 4)
new_g.addEdge("D", "E", 7)
new_g.addEdge("D", "F", 8)
new_g.addEdge("E", "F", 9)
new_g.addEdge("E", "G", 5)
new_g.addEdge("F", "G", 10)

new_g.kruskalAlgo()

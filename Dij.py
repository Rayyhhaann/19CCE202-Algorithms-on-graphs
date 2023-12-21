from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

    def visualize(self):
        for node in self.nodes:
            neighbors = self.edges[node]
            for neighbor in neighbors:
                distance = self.distances[(node, neighbor)]
                print(f"{node} --{distance}--> {neighbor}")

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    return visited, path

# Create a different graph
customGraph = Graph()
customGraph.addNode("X")
customGraph.addNode("Y")
customGraph.addNode("Z")
customGraph.addNode("W")
customGraph.addNode("K")
customGraph.addNode("L")
customGraph.addNode("M")
customGraph.addEdge("X", "Y", 3)
customGraph.addEdge("X", "Z", 7)
customGraph.addEdge("Y", "Z", 2)
customGraph.addEdge("Y", "W", 5)
customGraph.addEdge("Z", "K", 4)
customGraph.addEdge("W", "L", 6)
customGraph.addEdge("W", "M", 1)
customGraph.addEdge("K", "L", 8)
customGraph.addEdge("L", "M", 9)

# Visualize the different graph
print("Graph Visualization:")
customGraph.visualize()

# Run Dijkstra's algorithm
initial_node = "X"
shortest_distances, shortest_paths = dijkstra(customGraph, initial_node)

# Display the results
print("\nShortest Distances:")
for node, distance in shortest_distances.items():
    print(f"From {initial_node} to {node}: {distance}")

print("\nShortest Paths:")
for node, path in shortest_paths.items():
    print(f"Path to {node}: {' -> '.join(path + [node])}")
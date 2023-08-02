class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Default dictionary to store the graph

    # Function to add an edge to the graph
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Utility function used to print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to all other vertices 
    # using Bellman-Ford algorithm. The function also detects negative weight cycle
    def bellman_ford(self, src):

        # Initialize distance from src to all other vertices as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Relax all edges |V| - 1 times.
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Look for negative weight cycle. If cycle is there, then Bellman-Ford 
        # does not work
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found! Print distances
        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)

from collections import defaultdict

class Graph:
    """A Graph class to represent a directed graph using adjacency list representation."""
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        """Add edge into the graph"""
        self.graph[s].append(d)

    def dfs(self, d, visited_vertex):
        """
        A function used to print a DFS of the graph from a given vertex.
        This function is used by print_scc().
        """
        visited_vertex[d] = True
        print(d, end=' ')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        """
        A recursive function that fills up stack with vertices (starting from a given vertex)
        present in DFS starting from v.
        """
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.append(d)

    def transpose(self):
        """
        A function to get the transpose of the graph.
        It returns a new graph where the edges of the source graph are reversed.
        """
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        """
        The main function that finds and prints all strongly connected components.
        """
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()
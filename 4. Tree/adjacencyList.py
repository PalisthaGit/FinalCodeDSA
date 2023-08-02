class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [None] * self.num_vertices

    def add_edge(self, source, destination):
        """Add an edge from source to destination."""
        node = Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        """Print the graph."""
        for i in range(self.num_vertices):
            print(f"Adjacency list of vertex {str(i)}:", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    num_vertices = 5

    # Create a graph and add edges
    graph = Graph(num_vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
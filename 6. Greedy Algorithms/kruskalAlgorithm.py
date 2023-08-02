class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, vertex1, vertex2, weight):
        self.edges.append([vertex1, vertex2, weight])

    # Find set of an element i (uses path compression technique)
    def find_set(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_set(parent, parent[i])

    # Perform union of two subsets 
    def union_sets(self, parent, rank, x, y):
        xroot = self.find_set(parent, x)
        yroot = self.find_set(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            # If ranks are same, make one as root and increment its rank
            parent[yroot] = xroot
            rank[xroot] += 1

    # Implement Kruskal algorithm
    def kruskal_algorithm(self):
        result = []
        i, edge_count = 0, 0

        # Sort edges in increasing order on the basis of their weight
        self.edges.sort(key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        while edge_count < self.num_vertices - 1:
            vertex1, vertex2, weight = self.edges[i]
            i = i + 1
            x = self.find_set(parent, vertex1)
            y = self.find_set(parent, vertex2)

            # If including this edge does not cause a cycle, include it in result
            if x != y:
                edge_count += 1
                result.append([vertex1, vertex2, weight])
                self.union_sets(parent, rank, x, y)

        # Print the resultant MST
        for vertex1, vertex2, weight in result:
            print(f"{vertex1} -- {vertex2} == {weight}")


# Create a graph and add edges
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

# Run Kruskal's algorithm
g.kruskal_algorithm()

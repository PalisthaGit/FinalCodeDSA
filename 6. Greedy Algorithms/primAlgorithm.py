def prims_algorithm(num_vertices, graph):
    INF = 9999999
    # Initialize the array to track selected vertices
    selected_vertices = [0] * num_vertices
    # Number of edges initially
    num_edges = 0

    # Start from vertex 0
    selected_vertices[0] = True

    print("Edge : Weight\n")

    while num_edges < num_vertices - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(num_vertices):
            if selected_vertices[i]:
                for j in range(num_vertices):
                    if not selected_vertices[j] and graph[i][j]:
                        # Not yet selected and there is an edge
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f"{x}-{y}:{graph[x][y]}")
        selected_vertices[y] = True
        num_edges += 1

# Adjacency matrix
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

# Number of vertices
V = 5

prims_algorithm(V, G)

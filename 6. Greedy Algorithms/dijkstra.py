# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

def find_vertex_to_visit(visited_and_distance):
    min_distance = float('inf')
    vertex = -1
    for index, (visited, distance) in enumerate(visited_and_distance):
        if not visited and distance < min_distance:
            min_distance = distance
            vertex = index
    return vertex

def dijkstra_algorithm(vertices, edges):
    num_of_vertices = len(vertices[0])
    visited_and_distance = [[0, 0]] + [[0, float('inf')] for _ in range(num_of_vertices - 1)]
    
    for _ in range(num_of_vertices):
        to_visit = find_vertex_to_visit(visited_and_distance)
        for neighbor_index in range(num_of_vertices):
            if vertices[to_visit][neighbor_index] == 1 and not visited_and_distance[neighbor_index][0]:
                new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance
        visited_and_distance[to_visit][0] = 1

    # Printing the distance
    for i, (_, distance) in enumerate(visited_and_distance):
        print(f"Distance of {chr(ord('a') + i)} from source vertex: {distance}")

dijkstra_algorithm(vertices, edges)

# The number of vertices
num_vertices = 4

INF = 999


# Algorithm implementation
def floyd_warshall(graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Adding vertices individually
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
     [2, 0, INF, 4],
     [INF, 1, 0, INF],
     [INF, INF, 2, 0]]
floyd_warshall(G)

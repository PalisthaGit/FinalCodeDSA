import collections

# BFS algorithm
def bfs(graph, start_node):
    # Create a set to store visited nodes and a queue to visit nodes in BFS order
    visited, queue = set(), collections.deque([start_node])
    visited.add(start_node)

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # Visit all the neighbours of the dequeued vertex
        # If the neighbour has not been visited, mark it as visited and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)

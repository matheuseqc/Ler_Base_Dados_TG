import os
import sys

def christofides_tsp(dist_matrix):
    n = len(dist_matrix)
    path = [0]  # Start from point 0
    visited = [False] * n
    visited[0] = True

    for _ in range(n - 1):
        current = path[-1]
        next_node = None
        min_distance = sys.maxsize

        for neighbor in range(n):
            if not visited[neighbor] and dist_matrix[current][neighbor] < min_distance:
                next_node = neighbor
                min_distance = dist_matrix[current][neighbor]

        path.append(next_node)
        visited[next_node] = True

    # Return to starting point
    path.append(path[0])

    return path, calculate_path_length(path, dist_matrix)

def calculate_path_length(path, dist_matrix):
    length = 0
    for i in range(len(path) - 1):
        length += dist_matrix[path[i]][path[i + 1]]
    return length

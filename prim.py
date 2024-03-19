from heapq import heappop, heappush

def prim_tsp(dist_matrix):
    """
    This function implements the Traveling Salesman Problem (TSP) using Prim's algorithm.

    Args:
        dist_matrix (list of lists): Distance matrix representing distances between points.

    Returns:
        tuple: A tuple containing the optimal path and its length.
    """
    n = len(dist_matrix)
    if n == 0:
        return [], 0  # Return empty path and length if no points

    path = [0]  # Start from point 0
    length = 0

    # Build the minimum spanning tree until all points are visited
    while len(path) < n:
        next_point = None
        min_distance = float('inf')

        # Find the nearest neighbor not yet in the path
        for i in range(n):
            if i not in path:
                if dist_matrix[path[-1]][i] < min_distance:
                    next_point = i
                    min_distance = dist_matrix[path[-1]][i]

        # Add the nearest neighbor to the path
        path.append(next_point)
        length += min_distance

    # Add the distance from the last point back to the starting point
    length += dist_matrix[path[-1]][path[0]]

    return path, length

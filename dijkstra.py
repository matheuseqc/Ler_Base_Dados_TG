def dijkstra_tsp(dist_matrix):
    """
    This function implements the Traveling Salesman Problem (TSP) using Dijkstra's algorithm.

    Args:
        dist_matrix (list of lists): Distance matrix representing distances between points.

    Returns:
        tuple: A tuple containing the optimal path and its length.
    """
    n = len(dist_matrix)
    all_points_set = set(range(n))

    # Memoization to store optimal distances and previous points
    memo = {(tuple([i]), i): tuple([0, None]) for i in range(n)}
    queue = [(tuple([i]), i) for i in range(n)]  # Initialize the queue with all starting points

    # Dijkstra's algorithm to find the shortest paths
    while queue:
        prev_visited, prev_last_point = queue.pop(0)
        prev_dist, _ = memo[(prev_visited, prev_last_point)]

        # Find the points to visit next
        to_visit = all_points_set.difference(set(prev_visited))
        for new_last_point in to_visit:
            new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
            new_dist = prev_dist + dist_matrix[prev_last_point][new_last_point]

            # Update memo if a shorter path is found
            if (new_visited, new_last_point) not in memo:
                memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
                queue += [(new_visited, new_last_point)]
            else:
                if new_dist < memo[(new_visited, new_last_point)][0]:
                    memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)

    # Retrace the optimal path
    optimal_path, optimal_length = retrace_optimal_path(memo, n)

    return optimal_path, optimal_length

def retrace_optimal_path(memo: dict, n: int) -> [[int], int]:
    """
    Retrace the optimal path from the memoized data.

    Args:
        memo (dict): Memoized data containing optimal distances and previous points.
        n (int): Number of points.

    Returns:
        tuple: A tuple containing the optimal path and its length.
    """
    points = tuple(range(n))

    min_dist = None
    end_point = None
    # Find the end point with the minimum distance
    for k in range(n):
        if (points, k) in memo:
            cur_dist, _ = memo[(points, k)]
            if min_dist is None or cur_dist < min_dist:
                min_dist = cur_dist
                end_point = k

    # Retrace the path from end to start
    optimal_path = [end_point]
    for _ in range(n - 1):
        _, next_point = memo[(points, end_point)]
        optimal_path.insert(0, next_point)

        # Update points and end_point for the next iteration
        points = tuple(sorted(set(points).difference({end_point})))
        end_point = next_point

    return optimal_path, min_dist

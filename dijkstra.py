def dijkstra_tsp(dist_matrix):
    n = len(dist_matrix)
    all_points_set = set(range(n))

    # memo keys: tuple(sorted_points_in_path, last_point_in_path)
    # memo values: tuple(length_of_shortest_path, previous_last_point)
    memo = {(tuple([i]), i): tuple([0, None]) for i in range(n)}
    queue = [(tuple([i]), i) for i in range(n)]

    while queue:
        prev_visited, prev_last_point = queue.pop(0)
        prev_dist, _ = memo[(prev_visited, prev_last_point)]

        to_visit = all_points_set.difference(set(prev_visited))
        for new_last_point in to_visit:
            new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
            new_dist = prev_dist + dist_matrix[prev_last_point][new_last_point]

            if (new_visited, new_last_point) not in memo:
                memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
                queue += [(new_visited, new_last_point)]
            else:
                if new_dist < memo[(new_visited, new_last_point)][0]:
                    memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)

    optimal_path, optimal_length = retrace_optimal_path(memo, n)

    return optimal_path, optimal_length


def retrace_optimal_path(memo: dict, n: int) -> [[int], int]:
    points = tuple(range(n))

    min_dist = None
    end_point = None
    for k in range(n):
        if (points, k) in memo:
            cur_dist, _ = memo[(points, k)]
            if min_dist is None or cur_dist < min_dist:
                min_dist = cur_dist
                end_point = k

    optimal_path = [end_point]
    for _ in range(n - 1):
        _, next_point = memo[(points, end_point)]
        optimal_path.insert(0, next_point)

        points = tuple(sorted(set(points).difference({end_point})))
        end_point = next_point

    return optimal_path, min_dist
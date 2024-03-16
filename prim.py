from heapq import heappop, heappush

def prim_tsp(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    min_edge = [float('inf')] * n
    selected_edge = [-1] * n
    min_edge[0] = 0
    queue = [(0, 0)]
    while queue:
        _, v = heappop(queue)
        visited[v] = True
        for to in range(n):
            if dist_matrix[v][to] < min_edge[to] and not visited[to]:
                min_edge[to] = dist_matrix[v][to]
                selected_edge[to] = v
                heappush(queue, (min_edge[to], to))
    path = []
    current = 0
    while current != -1:
        path.append(current)
        current = selected_edge[current]
    path.append(0)
    length = sum(dist_matrix[path[i-1]][path[i]] for i in range(1, n+1))
    return path, length
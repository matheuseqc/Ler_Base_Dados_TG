from heapq import heappop, heappush

def prim_tsp(dist_matrix):
    n = len(dist_matrix)
    if n == 0:
        return [], 0  

    path = [0]  
    length = 0

    while len(path) < n:
        
        next_point = None
        min_distance = float('inf')
        for i in range(n):
            if i not in path: 
                if dist_matrix[path[-1]][i] < min_distance:
                    next_point = i
                    min_distance = dist_matrix[path[-1]][i]

       
        path.append(next_point)
        length += min_distance


    length += dist_matrix[path[-1]][path[0]]

    return path, length
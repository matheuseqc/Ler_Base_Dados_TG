import os
from itertools import permutations
import sys

# Base directory for data reading
base_directory = '/read_data'

def brute_force_tsp(dist_matrix):
    """
    This function implements the brute force approach for solving the Traveling Salesman Problem (TSP).

    Args:
        dist_matrix (list of lists): Distance matrix representing distances between points.

    Returns:
        tuple: A tuple containing the optimal path and its length.
    """
    n = len(dist_matrix)
    min_path = None
    min_distance = sys.maxsize

    # Generate all possible tours
    for tour in permutations(range(n)): 
        # Calculate the total distance of the tour
        distance = sum(dist_matrix[tour[i - 1]][tour[i]] for i in range(n))  

        # Update the minimum distance and path if a shorter tour is found
        if distance < min_distance:  
            min_distance = distance
            min_path = tour

    return min_path, min_distance

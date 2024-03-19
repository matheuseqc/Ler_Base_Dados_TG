import os
from itertools import permutations
import sys

# Base directory for data reading
base_directory = '/read_data'

def brute_force_tsp(dist_matrix):
    """
    Força bruta para resolver o problema do PCV.
    Args:
        dist_matrix (list of lists): Matriz representando a distância entre pontos.
    Returns:
        tuple: Uma tupla contendo o melhor caminho e seu tamanho.
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

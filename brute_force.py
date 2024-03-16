import signal
import os
from itertools import permutations
import sys

pasta_base = '/ler_base_de_dados'
# Define the handler for the alarm signal
def handler(signum, frame):
    raise Exception("O código executou por mais de 12 horas")

# Set the signal handler
signal.signal(signal.SIGALRM, handler)

def brute_force_tsp(dist_matrix):
    n = len(dist_matrix)
    min_path = None
    min_distance = sys.maxsize

    for tour in permutations(range(n)):  # Generate all possible tours
        distance = sum(dist_matrix[tour[i-1]][tour[i]] for i in range(n))  # Calculate the total distance of the tour

        if distance < min_distance:  # If this tour is shorter, update min_distance and min_path
            min_distance = distance
            min_path = tour

    return min_path, min_distance

# Set the alarm for 12 hours
signal.alarm(12 * 60 * 60)

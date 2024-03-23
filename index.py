import os
import time
from utils import ler_matriz_distancias
from brute_force import brute_force_tsp
from dijkstra import dijkstra_tsp
from prim import prim_tsp
from christofides import christofides_tsp
from func_timeout import func_timeout, FunctionTimedOut

# List of files to process
arquivos = ['teste.txt', 'att48_d.txt', 'dantzig42_d.txt', 'fri26_d.txt', 'gr17_d.txt', 'p01_d.txt']

# Base directory for reading data
pasta_base = 'ler_base_dados'

# Selected algorithm for solving TSP
algoritmo = christofides_tsp

start_time = time.time()  # Start timing the execution

# Iterate over each file
for arquivo in arquivos:
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    if elapsed_time > 12 * 60 * 60:  # If execution time exceeds 12 hours
        print("The code has been running for more than 12 hours")
        break

    # Construct full path to the file
    caminho_completo = os.path.join(pasta_base, arquivo)

    # Read distance matrix from the file
    matriz_distancias = ler_matriz_distancias(caminho_completo)

    # Print the distance matrix
    print("Distance matrix:" + str(matriz_distancias) + "\n")

    try:
        print(f"\033[1mCalculating the shortest route for {arquivo}...\033[0m")
        # Execute the selected algorithm with a timeout
        shortest_route, shortest_length = func_timeout(12 * 60 * 60 - elapsed_time, algoritmo, args=(matriz_distancias,))
        print(f"\033[1;32m\nThe shortest route for {arquivo} is: {shortest_route}, with length {shortest_length}.\033[0m")
    except FunctionTimedOut:
        print(f"The file {arquivo} did not finish executing within the time limit")

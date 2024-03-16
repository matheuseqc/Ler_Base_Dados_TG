import os
import time
from utils import ler_matriz_distancias
from brute_force import brute_force_tsp
from dijkstra import dijkstra_tsp
from prim import prim_tsp
from func_timeout import func_timeout, FunctionTimedOut

arquivos = ['teste.txt','att48_d.txt', 'dantzig42_d.txt', 'fri26_d.txt', 'gr17_d.txt', 'p01_d.txt']
pasta_base = 'ler_base_dados'
algoritmo = prim_tsp

start_time = time.time()  # Start the timer

for arquivo in arquivos:
    elapsed_time = time.time() - start_time
    if elapsed_time > 12 * 60 * 60:  # If more than 12 hours have passed
        print("O código executou por mais de 12 horas")
        break

    caminho_completo = os.path.join(pasta_base, arquivo)
    matriz_distancias = ler_matriz_distancias(caminho_completo)
    print("Matriz de distâncias:" + str(matriz_distancias) + "\n")

    try:
        print(f"\033[1mCalculando a menor rota para {arquivo}...\033[0m")
        shortest_route, shortest_length = func_timeout(12 * 60 * 60 - elapsed_time, algoritmo, args=(matriz_distancias,))
        print(f"\033[1;32m\nA menor rota para {arquivo} é: {shortest_route}, com comprimento {shortest_length}.\033[0m")
    except FunctionTimedOut:
        print(f"O arquivo {arquivo} não terminou de executar no tempo limite")
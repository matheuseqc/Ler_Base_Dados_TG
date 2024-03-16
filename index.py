import os
from utils import ler_matriz_distancias
from brute_force import brute_force_tsp

arquivos = ['att48', 'dantzig42', 'fri26', 'gr17', 'p01']

pasta_base = 'ler_base_dados'
arquivos = ['att48_d.txt', 'dantzig42_d.txt', 'fri26_d.txt', 'gr17_d.txt', 'p01_d.txt']
algoritmo = brute_force_tsp

try: 
    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta_base, arquivo)
        matriz_distancias = ler_matriz_distancias(caminho_completo)
        
        print(f"\033[1mCalculando a menor rota para {arquivo}...\033[0m")
        shortest_route, shortest_length, total_permutations = algoritmo(matriz_distancias)
        print(f"\033[1;32m\nA menor rota para {arquivo} é: {shortest_route}, com comprimento {shortest_length}.\033[0m")
        print(f"Número de permutações: {total_permutations}\n----------------------------------")
except Exception as e:
    print(e)

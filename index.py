import os

def ler_matriz_distancias(arquivo):
    matriz_distancias = []  # Lista de listas para armazenar os dados

    with open(arquivo, 'r') as file:
        linhas = file.readlines()

        for linha in linhas:
            numeros = [int(numero) for numero in linha.split()]
            matriz_distancias.append(numeros)

    return matriz_distancias

pasta_base = 'ler_base_dados'
arquivos = ['att48_d.txt', 'dantzig42_d.txt', 'fri26_d.txt', 'gr17_d.txt', 'p01_d.txt']

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta_base, arquivo)
    matriz_distancias = ler_matriz_distancias(caminho_completo)

    # Exibindo a matriz de distâncias para cada arquivo
    print(f'Matriz de distâncias para {arquivo}:')
    print(matriz_distancias)
    print('\n' + '='*40 + '\n')  # Separador entre os arquivos

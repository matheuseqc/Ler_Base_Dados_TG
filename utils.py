def ler_matriz_distancias(arquivo):
    matriz_distancias = []  

    with open(arquivo, 'r') as file:
        linhas = file.readlines()

        for linha in linhas:
            numeros = [int(numero) for numero in linha.split()]
            matriz_distancias.append(numeros)

    return matriz_distancias
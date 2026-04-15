# matrix.py

def transpor_matriz(matriz):
    if not matriz:
        return []

    linhas = len(matriz)
    colunas = len(matriz[0])

    transposta = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    return transposta


def multiplicar_matriz(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        print("Erro: Número de colunas de A deve ser igual ao número de linhas de B.")
        return None

    resultado = []

    for i in range(len(matriz_a)):
        linha_resultado = []
        for j in range(len(matriz_b[0])):
            soma = 0
            for k in range(len(matriz_b)):
                soma += matriz_a[i][k] * matriz_b[k][j]
            linha_resultado.append(soma)

        resultado.append(linha_resultado)

    return resultado

# main.py

from matrix import transpor_matriz, multiplicar_matriz

# Teste de Transposição
A = [[1, 2], [3, 4], [5, 6]]

print("Matriz A:")
print(A)

transposta = transpor_matriz(A)

print("\nTransposta de A:")
print(transposta)

# Teste de Multiplicação
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("\nMatriz A:")
print(A)

print("\nMatriz B:")
print(B)

resultado = multiplicar_matriz(A, B)

print("\nResultado da multiplicação:")
print(resultado)

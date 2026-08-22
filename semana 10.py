# Definir matriz 3x3 con números enteros
matriz = [
    [12, 14, 16],
    [11, 13, 15],
    [17, 18, 19]
]

# Recorrer e imprimir todos los valores usando ciclos
print("Valores de la matriz 3x3:\n")
for fila in range(3):
    for columna in range(3):
        print(f"Elemento [{fila}][{columna}] = {matriz[fila][columna]}")
    print()
# Reserva de asientos de cine

## Descripción
Programa en Python que gestiona la reserva de un asiento en una sala de cine de 3 filas por 4 columnas.

- `0` = asiento libre
- `1` = asiento reservado

## Funcionamiento
1. Se crea una matriz de 3 x 4 inicializada con ceros.
2. El programa solicita la fila y la columna del asiento.
3. El asiento seleccionado cambia de `0` a `1`.
4. Se muestra toda la matriz usando dos bucles anidados.


## Ejemplo de ejecución

```text
Ingrese fila (0 a 2): 1
Ingrese columna (0 a 3): 2

Estado de la sala:
0 0 0 0
0 0 1 0
0 0 0 0
```

## Ejecución
Guarda el archivo `reserva_cine.py` y ejecútalo con:

```bash
python reserva_cine.py
```

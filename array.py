import numpy as np;

#lista de python
lista = [1,2,3,4,5,6,7,8,9];
print(lista);

# llevar la lista a numpy
arrayLista = np.array(lista);
print(arrayLista);

print(type(arrayLista));

matriz = [[1,2,3], [4,5,6], [7,8,9]];
nuevaMatriz = np.array(matriz);
print(nuevaMatriz);

# INDEXING
print(arrayLista);

print(arrayLista[1]);

print(arrayLista[0] + arrayLista[5]);

print(nuevaMatriz);

print(nuevaMatriz[0]);

# Primer valor de filas, segundo de columnas
print(nuevaMatriz[0, 1]);

print(arrayLista);

# Muestra los valores en un rango de posiciones determinado
print(arrayLista[0:3]);

print(arrayLista[1:6]);

print(nuevaMatriz);

# El primer valor es a nivel de filas, el segundo de columnas
print(nuevaMatriz[1:, 0:2]);
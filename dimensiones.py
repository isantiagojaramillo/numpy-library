import numpy as np;

scalar = np.array(42);
print(scalar);
print(scalar.ndim); # verifica el número de dimensiones

vector = np.array([1,2,3]);
print(vector);
print(vector.ndim);

matriz = np.array([[1,2,3], [4,5,6], [7,8,9]]);
print(matriz);
print(matriz.ndim);

tensor = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]);
print(tensor);
print(tensor.ndim);

# Agregar o eliminar dimensiones
vector2 = np.array([1,2,3], ndmin=10); # se define con limite de dimensiones
print(vector2);
print(vector2.ndim);

expandDimension = np.expand_dims(np.array([1,2,3]), axis=0); # expandir las dimensiones a nivel de columnas
print(expandDimension);
print(expandDimension.ndim);

print(vector2, vector2.ndim);
vector3 = np.squeeze(vector2); # corregir el numero de dimensiones que se estan usando
print(vector3, vector3.ndim);
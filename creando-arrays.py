import numpy as np;

list(range(0,10));

arreglo = np.arange(0,10); # creando un array
print(arreglo);

arrayZeros = np.zeros((3,3)); # GENERA UN ARRAY COMPUESTO DE CEROS
print(arrayZeros);



arrayOnes = np.ones((10,5)); # Genera un array compuesto por unos
print(arrayOnes);

array2 = np.linspace(0,10,10); # GENERA UN ARRAY DESDE 0 HASTA 10 CON 10 DATOS
print(array2);

matriz = np.eye(4); # CREA UNA MATRIZ CON LA DIAGONAL EN 1 y el resto en 0
print(matriz);

randomNumber = np.random.rand(); # Genera un número random entre 0 y 1
print(randomNumber);

array3 = np.random.rand(4); # Genera un array con 4 números aleatorios entre 0 y 1
print(array3);

array4 = np.random.rand(4, 4); # Genera una matriz de 4x4 con números aleatorios entre 0 y 1
print(array4);

enteroAleatorio = np.random.randint(1,15); #Genera un número entero aleatorio entre 1 y 15
print(enteroAleatorio);

matriz2 = np.random.randint(1,100, (10,10)); # Genera una matriz de 10x10 con datos enteros de 1 a 100
print(matriz2);
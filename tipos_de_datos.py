import numpy as np;

array = np.array([1,2,3,4]);
print(array);

# dtype nos muestra el tipo de dato del array
print(array.dtype);

array = np.array([1,2,3,4], dtype='float64');
print(array.dtype);

# cambio en el tipo de datos de int a float
arrayInt = np.array([0,9,8,7,6]);
print(arrayInt);

arrayFloat = arrayInt.astype(np.float64);
print(arrayFloat);

# A tipo booleano
arrayBool = arrayInt.astype(np.bool_);
print(arrayBool);

# a tipo string
arrayStr = arrayInt.astype(np.string_);
print(arrayStr);
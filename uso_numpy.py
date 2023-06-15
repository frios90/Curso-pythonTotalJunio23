# import numpy              # Cargar el modulo numpy, o bien
import numpy as np        # cargar el modulo numpy, llamándolo np, o bien
import sys

a = np.array((1,2,3))
print(a)
print("")
a = np.array([[1,2], [10,20]])
print(a)
print("")

# Si quieres crear un array unidimensional con solamente 2 elementos utilizas el siguiente código:
b= np.empty(2)
print(b)

# Si quieres crear un array bidimensional debes indicar el número de filas y columnas que tendrá el array, como se indica a continuación:

c = np.empty( [2, 2])
print(c)

# Para crear un array unidimensional con 2 elementos, ambos ceros utilizamos el siguiente código:
d = np.zeros(3)
print("d")
print(d)

#Por su parte para crear un array bidimensional debes indicar el número de filas y columnas que tendrá el array:
e = np.zeros([5,8])
print("e")
print(e)

np.ones(2)
np.ones([2, 3])

# Para crear un array con un rango de elementos, por ejemplo 3, escribimos el siguiente código:
f = np.arange(3)
print("f")
print(f)

# Si quieres crear un array con un rango de elementos, con números entre 2 y 7, por ejemplo, escribes el siguiente código:
g = np.arange(2,7)
print("g")
print(g)

# Para crear un array un con elementos aleatorios debemos utilizar la siguiente instrucción e indicar el número de filas y columnas que tendrá el array.

h = np.random.rand(2,3)
print("h")
print (h)

# Añadir elementos

i = np.array((1,2,3))
i = np.append(i, (4,5))
print("i")
print(i)

# Eliminar elementos

j = np.array((1,2,3))
j = np.delete(j,1)
print("j")
print(j)

# Conocer la forma del array

k = np.array([[1,2,8],[65,32,6],[3,41,6]])
print("k")
print(k)
print(k.shape)
j = np.delete(k,1)
print(j)


#Conocer el número de dimensiones del array

l = np.array([[1,2,8],[65,32,6],[3,41,6]])
print("l")
print(l)
print(l.ndim)

# Conocer el número de elementos del array
print(l.size)
print(l[0].size)

# Conocer el tipo de datos del array
print(l.dtype)

print("########################################")
print("Funciones matemáticas")
print("########################################")
print("")


# Velocidad de NumPy
S= range(1000)
print(sys.getsizeof(5)*len(S))
D= np.arange(1000)
print(D.size*D.itemsize)
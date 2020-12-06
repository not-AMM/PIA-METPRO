import numpy as np
import random
from functools import reduce
# j representa los años
# i representa los meses
# k representa los departamentos

mj = []
M = []
# Inicializamos la variable 'i', tomar en cuenta que en Python se comienza en 0.
i = 1
# El primer bucle representa una iteración sobre los meses.
while i <= 12:
    j = 1
    # El segundo bucle representa una iteración sobre los años.
    while j <= 4:
        k = 1
        # El tercer bucle representa una iteración sobre los departamentos.
        while k <= 3:
            # Generamos el arreglo tridimensional de 12 * 4 * 3
            M = [[[random.randint(400, 1500) for k in range(3)] for j in range(4)] for i in range(12)]
            # Imprimimos el mes, año, departamento y el valor de producción de dicho momento {el valor está pendiente} 
            print("Producción de: | Mes: " + str(i) + " | Año: " + str(j) + " | Departamento: " + str(k) + " |")
            # Creamos un vector bidimensional con todos los valores
            V =  reduce(list.__add__, M, [])
            # Terminamos por crear un vector unidimensional con todos los valores
            V =  reduce(list.__add__, V, [])
            k = k + 1 
        else:
            j = j + 1
    else:
        i = i + 1   
else:
    k = 1
    M = np.array(M,dtype = object)
    print("Dimensiones: " + str(M.shape))
    print(M)
    print(V)
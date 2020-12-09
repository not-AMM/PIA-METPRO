import numpy as np
import random
from functools import reduce
# j representa los años
# i representa los meses
# k representa los departamentos

# Comienza la primera parte del primer programa
M = []
# Inicializamos la variable 'i', tomar en cuenta que en Python se comienza en 0.
i = 0
# El primer bucle representa una iteración sobre los meses.
while i <= 11:
    j = 0
    # El segundo bucle representa una iteración sobre los años.
    while j <= 3:
        k = 0
        # El tercer bucle representa una iteración sobre los departamentos.
        while k <= 2:
            # Generamos el arreglo tridimensional de 12 * 4 * 3
            ML = [[[random.randint(400, 1500) for k in range(2)] for j in range(3)] for i in range(11)]
            M = np.array(ML,dtype=object)
            # valor = M[i,j,k]
            k = k + 1 
        else:
            j = j + 1
    else:
        i = i + 1   
else:
    # Comienza la segunda parte del primer programa
    # Imprimimos la matriz
    print(M)
    # Obtenemos la suma de la producción de cada departamento
    dpt1 = M.T[0]
    dpt1 = dpt1.tolist()
    dpt1 = reduce(list.__add__, dpt1, [])
    prod1 = sum(dpt1)
    dpt2 = M.T[1]
    dpt2 = dpt2.tolist()
    dpt2 = reduce(list.__add__, dpt2, [])
    prod2 = sum(dpt2)
    dpt3 = M.T[2]
    dpt3 = dpt3.tolist()
    dpt3 = reduce(list.__add__, dpt3, [])
    prod3 = sum(dpt3)
    prod = []
    prod.append(prod1)
    prod.append(prod2)
    prod.append(prod3)
    print(" Producción del año 1: $" + str(prod1) + "\n Producción del año 2: $" + str(prod2) + "\n Producción del año 3: $" + str(prod3))
    # Terminamos las pruebas y procedemos con el programa---------------------------------
    mayor = 0
    k = 1
    while k <= 2:
        if prod[mayor] > prod[k]:
            mayor = mayor
        else:
            mayor = k   
        k = k + 1
    else:
        print("Departamento con más producción:" + str(mayor + 1))

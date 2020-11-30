import numpy as np
from random import random
from random import sample as generar
# j representa los años
# i representa los meses
# k representa los departamentos

prodmens = []
# Se genera una lista con valores desde el 400 hasta el 1500
valores = range(400,1500)
# La función 'generar' elige 144 números al azar y los guarda en una lista
valores = generar(valores,k=144)
i = 1
while i <= 12:
    j = 1
    while j <= 4:
        k = 1
        while k <= 3:
            M = np.array((i,j,k))
            # Los valores al azar representan la producción de cada mes de cada departamento
            for x in valores:
                print("Producción del mes " + str(i) + " del año " + str(j) + " del departamento " + str(k) + ": " + str(x))
                prod = x
            prodmens.append(prod)
            k = k + 1 
        else:
            j = j + 1
    else:
        i = i + 1
else:
    print(prodmens)
    suma = np.array(suma)
    print(suma)
    print(suma.shape)
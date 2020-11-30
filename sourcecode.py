import numpy as np
from random import random
from random import sample as generar
# j representa los años
# i representa los meses
# k representa los departamentos

dp1 = [] # Necesito encontrar un modo de dividir las listas para encontrar lo que pertenece a cada departamento
dp2 = [] # o, en su defecto, encontrar el modo de guardar todo en un array y extraerlo cuando lo necesite
dp3 = [] # como si fueran coordenadas
vk = []
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
# Convetimos la lista de valores en un arreglo unidimensional
    np.array(prodmens)
# Inicializamos la variable k para proceder al segundo paso
    k = 1 
    while k <= 3:
        i = 1
        while i <= 12:
            j = 1
            while j <= 4:
                vk=[] 
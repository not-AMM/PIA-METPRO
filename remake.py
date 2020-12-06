# Programa de pruebas con arreglos
# Importamos las librerías necesarias
import random
import numpy as np

# Podría decirse que un array 3D es una lista, dentro de una lista, dentro de una lista.
# Usar este método para el PIA de METPRO.

def arreglo3x3x3():
    i = 1
    u = []
    w = []
    while i <=3:
        # Creo una lista de 3 ceros
        v = ['0', '0', '0']
        # Agrego la lista de 3 ceros a la lista 'w'
        w.append(v)
        # Agrego la lista 'w' a la lista 'u'
        u.append(w)
        i = i + 1
    else:
        u = np.array(u)
        print(u)
        print("Dimensiones del arreglo:" + str(u.shape)) 

def arreglo12x4x3():
    i = 1
    while i <= 12:
        j = 1
        while j <= 4:
            k = 1
            while k <= 3:
                # Se crea un arreglo 3D con valores random
                M = [[[random.randint(400, 1500) for i in range(3)] for j in range(4)] for k in range(12)]
                k = k + 1
            else:
                j = j + i
        else:
            i = i + 1
    else:
        M = np.array((M))                
        print(M)
        print(str(M.shape))

arreglo3x3x3()
arreglo12x4x3()

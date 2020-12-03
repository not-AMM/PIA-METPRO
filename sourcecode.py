import numpy as np
# j representa los años
# i representa los meses
# k representa los departamentos

# Inicializamos la variable 'i', aunque habrá que corregir porque en Python se comienza en 0.
i = 1
# El primer bucle representa una iteración sobre los meses.
while i <= 12:
    j = 1
    # El segundo bucle representa una iteración sobre los departamentos.
    while j <= 4:
        k = 1
        # El tercer bucle representa una iteración sobre los años.
        while k <= 3:
            # Creamos el array. Probablemente sería mejor hacer una lsita y convertirla en array.
            M = np.array((i,j,k))
            # Creamos una lista
            suma = []
            # COmenzaros a meter los datos
            prod = float(input("Producción del mes " + str(i) + " del año " + str(j) + " del departamento " + str(k) + ":"))
            suma.append(prod)
            suma = np.array(suma)
            k = k + 1 
        else:
            j = j + 1
    else:
        i = i + 1
else:
    k = 1
    while k <= 3:
        vk = []
        i = 1
        while i <= 12:
            j = 1
            while j <= 4:
                vk = suma[k]
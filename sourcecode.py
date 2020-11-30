import numpy as np
# j representa los años
# i representa los meses
# k representa los departamentos

i = 1
while i <= 12:
    j = 1
    while j <= 4:
        k = 1
        while k <= 3:
            M = np.array((i,j,k))
            suma = []
            prod = float(input("Producción del mes " + str(i) + " del año " + str(j) + " del departamento " + str(k) + ":"))
            suma.append(prod)
            k = k + 1 
        else:
            j = j + 1
    else:
        i = i + 1
else:
    print(suma)
    suma = np.array(suma)
    print(suma)
    print(suma.shape)
    k = 1
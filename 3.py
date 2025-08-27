"""
Calcular o número 휋 usando a serie:
pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
Comparar o resultado dependendo do número de termos usados na série com o verdadeiro valor de 휋 que pode ser obtidousando np.pi"""

import numpy as np

n = 100 # número de termos
div = np.arange(3,(n*2+3),2) # divisores

#print(div)

for i in range(0,n,2):
    div[i] = div[i]*-1

pi = 1

for i in div:
    pi += 1/i

print("pi calculado: {0}, numpy pi: {1}".format(pi*4, np.pi))
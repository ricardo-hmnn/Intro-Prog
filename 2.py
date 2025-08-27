"""Fazer um código que define um ponto de R² e imprime True ou False dependendo se o ponto está emcima ou embaixo da
reta y = x."""

import numpy as np

p = np.array(np.round([np.random.random(), np.random.random()], 2)) # (x,y)
print(p)

"""
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
#print(x,y)

for i in range(100):
    if(np.allclose(p[0], x[i], atol=0.005) == True):
        if(p[1] > y[i]):
            print("True")
        elif(p[1] < y[i]):
            print("False")
"""

if (p[0] < p[1]):
    print("True")
elif (p[0] > p[1]):
    print("False")

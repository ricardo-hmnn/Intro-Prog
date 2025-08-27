"""Repetir o exercício anterior para o caso em que a esfera está centrada em (0.25, 0.5, 0.75)."""

from numpy.random import default_rng
from math import sqrt

def pontosEsfera(a,b,c):
    rng = default_rng()
    j = 0
    for i in range(10):
        i = rng.integers(0,201,3)/100
        if (sqrt((i[0] - a)**2 + (i[1] - b)**2 + (i[2] - c)**2) > 1):
            j += 1
    return j
        
    

print(pontosEsfera(0.25,0.5,0.75))
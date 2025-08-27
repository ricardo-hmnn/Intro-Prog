"""Repetir o exercício anterior para o caso de pontos em R3 e uma esfera"""

from numpy.random import default_rng
from math import sqrt

prob = 0
n,v = 100,10000

for i in range(n):
    rng = default_rng()
    j = 0
    for i in range(v):
        i = rng.integers(0,201,3)/100
        if (sqrt(i[0]**2 + i[1]**2 + i[2]**2) <= 1):
            j += 1
    prob += j
prob = prob/(n*v)
print(prob) # fazendo n*v tender ao infinito, 6,5% 

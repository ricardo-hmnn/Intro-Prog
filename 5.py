"""Fazer um programa que cria 10 pontos inventados em R2 e imprime quantos desses pontos estão fora do círculo de raio 1
centrado na origem e quantos dentro."""

from numpy.random import default_rng
from math import sqrt

rng = default_rng()
pontos = []
for i in range(10):
    i = rng.integers(0,200,2)/100
    if (sqrt(i[0]**2 + i[1]**2 ) > 1):
        print(i)
    pontos.append(i)

print(pontos)
"""Fazer um código que define dois vetores vec1 e vec2 de tamanho 5 com números de ponto flutuante inventados. Depois cria
um outro vetor de números inteiros do mesmo tamanho, tal que na i-ésima posição ele toma o valor 1 se a componente
correspondente de vec1 é maior que a do vec2 e 0 em caso contrário."""

import numpy as np

rng = np.random.default_rng()

vec1 = rng.integers(0,1000, (5)) / 100
vec2 = rng.integers(0,1000, (5)) / 100
vec3 = np.zeros(5)

print(vec1, vec2)

for i in range(5):
    if(vec2[i] < vec1[i]):
        vec3[i] = 1
        
print(vec3)
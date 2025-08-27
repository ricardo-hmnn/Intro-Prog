'''
Fazer um script que define uma matriz randômica de dimensão
N x N e calcula a média dos valores dos seus elementos, tomando N = 10 , 100 , 500 , 1000. Pode usar a função de numpy
np.random.rand(N,N) que irá criar um array bidimensional (i.e., uma matriz) com N linhas e N colunas com de números
randômicos com valores entre 0 e 1 distribuidos uniformemente.'''


def mediaMatrizAleatoria(N):
    from numpy.random import rand

    soma1, soma2 = 0, 0
    matriz = rand(N,N)

    for i in matriz:
        soma1 += i
    for i in soma1:
        soma2 += i

    return (soma2 / (N**2))
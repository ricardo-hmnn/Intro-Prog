"""Fazer um script que define um vetor randômico de dimensão N e calcula a média dos valores das suas componentes
Considerar N = 10, 100, 1000, 10000, 100000, 1000000."""

def mediaVetor(n):
    from numpy import mean
    from numpy.random import rand

    """
    media = 0
    for i in vec:
        media += i
    media = (media/n)
    """
    vec = rand(n)
    return mean(vec)

print(mediaVetor(100))
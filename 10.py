'''
Fazer uma função que calcula o produto escalar de dois vetores
randômicos a e b de R³, calcula a sua magnitude e determina o
ângulo 𝜃 que eles formam, usando a fórmula.
'''

from numpy.random import rand
import numpy

def angEscalar(a, b):
    import numpy
    return numpy.arccos((numpy.dot(a,b)) / (numpy.linalg.norm(a) * numpy.linalg.norm(b)))

'''
modA = numpy.linalg.norm(a) #sqrt(a[0]**2 + a[1]**2 + a[2]**2)
modB = numpy.linalg.norm(b) #sqrt(b[0]**2 + b[1]**2 + b[2]**2)

if (modB == 0.0 or modA == 0.0):
    raise ArithmeticError("O ângulo entre um vetor nulo não é definido.")
elif (numpy.array_equal(a,b)):
    return 0
'''

a, b = rand(3),rand(3)
#a, b = numpy.array([2,1,-2]),numpy.array([4,4,2])

print(angEscalar(a,b))
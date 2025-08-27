'''
Fazer um gráfico da função f(x) = sin(mx) para diferentes
valores de 𝑚 considerando o intervalo x ∈ [0,2𝜋].
'''

import numpy as np
import matplotlib.pyplot as plt

def seno(m):
    x = np.linspace(0,2*np.pi,628)
    y = np.sin(m*x)
    plt.plot(x, y) 
    plt.title("Função seno(mx)")
    plt.show()

seno(9)
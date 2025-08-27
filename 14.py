"""
Fazer um gráfico da função f(x) = x^m para diferentes valores de m considerando o intervalo x ∈ [1,4]. 
Usar escala linear e escala loglog.
"""

import numpy as np
import matplotlib.pyplot as plt


def funcaoGrauM(m):
    x = np.linspace(1,4,300)
    y = x**m
    plt.plot(x, y) 
    plt.title("Função de grau m")
    plt.show()
    plt.loglog(x,y)
    plt.show()

funcaoGrauM(2)
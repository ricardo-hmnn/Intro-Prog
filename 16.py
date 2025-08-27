"""
Fazer um gráfico que mostra pontos distribuídos randomicamente na região do plano [0,2] x [-2,1].
"""

import numpy as np
import matplotlib.pyplot as plt

def pontosPlano():
    x = np.random.randint(0,200,size=(25))/(-100)
    y = np.random.randint(50,100,size=(25))/50
    i = [-2,0]# Pontos que definem 
    j = [2,1] # o plano 
    plt.scatter(i,j)
    plt.scatter(x,y)
    plt.show()
pontosPlano()
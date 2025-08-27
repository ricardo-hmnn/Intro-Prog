'''
Considerar 10 dados que são jogados, podendo sair números do 1 até o 6. Jogar os 10 dados 100000 vezes e construir um histograma que mostre
o comportamento da soma. Um histograma seria um gráfico de frequencia de um certo evento, ou seja, quantas vezes a soma
deu 10, quantas vezes a soma deu 11, quantas vezes a soma deu 12, ..., quantas vezes a soma deu 60. Para isto precissará usar a
função counts, bins = np.histogram(s) plt.stairs(counts, bins) em que s será um vetor que guardou o resultados das 100000
realizações. Pode usar a função np.random.randint(1,7,10) que irá gerar 10 número inteiros entre 1 e 6, com
'''

import matplotlib.pyplot as plt
import numpy as np

somas = np.sum(np.random.randint(1, 7, size=(100000, 10)), axis=1)

# Resolução problema dos buracos:
# As faixas (bins) são definidas a partir da diversidade dos dados, e se a amostra não for ridiculamente grande (aproximadamente 6^12 que é 
# 100x o inverso da menor probabilidade, o 10 (ou o 60), que tem 6^-10 de chance de aparecer) alguns valores simplesmente não aparecerão 
# (eu testei vadia). Então para resolver o problema o negocio é dividir o espaço manualmente com o arange

bins = np.arange(10,61,1)
counts, bins = np.histogram(somas,bins=bins)

#print(counts.shape, bins.shape, counts, bins) 

fig, ax = plt.subplots()

plt.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black')
#plt.stairs(counts,bins)

plt.title('Histograma gerado com NumPy e plotado com Matplotlib')
plt.xlabel('Somas')
plt.ylabel('Frequência')
#plt.show() se estiver nao der erro


plt.savefig("histograma.png")

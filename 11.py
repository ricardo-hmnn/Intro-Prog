'''
Fazer uma função que calcula o produto vetorial de dois vetores randômicos a e b de R³
'''

import numpy as np

a, b = np.array([1,-2,2]),np.array([-1,1,2])

def produtoVetorial(a,b): 
    import numpy as np
    return np.array([np.linalg.det(np.array([[a[1],a[2]],[b[1],b[2]]])),(-1)*np.linalg.det(np.array([[a[0],a[2]],[b[0],b[2]]])),np.linalg.det(np.array([[a[0],a[1]],[b[0],b[1]]]))])



print(produtoVetorial(a,b),np.linalg.cross(a,b))
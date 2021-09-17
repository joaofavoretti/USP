import numpy as np
from numpy import linalg

X = [1, 2, 3, 4]
Y = [3, 5, 6, 8]

grau = 1

def minQuadrados():
    
    # Cria vetores H
    H = np.zeros((grau + 1, len(X)))
    for i in range(len(H)):
        for j in range(len(H[0])):
            H[i][j] = pow(X[j], i)
   
    # Sistema Ax = b
    A = np.zeros((grau + 1, grau + 1))
    b = np.zeros(grau + 1)

    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = H[i].dot(H[j])
       
        b[i] = H[i].dot(Y)

    # Resolver sistema Ax = b
    x = np.linalg.solve(A,b)
    for i in range(len(x)):
        print("c"+str(i)+" = ", x[i])


if __name__ == '__main__':
    minQuadrados()


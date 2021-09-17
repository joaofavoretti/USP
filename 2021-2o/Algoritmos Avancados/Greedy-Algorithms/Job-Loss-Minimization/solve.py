"""
Job Sequencing - Loss minimization
Greedy Algorithm
author: Joao Pedro Favoretti
"""

# Numero de casos de teste
T = int(input())

# Loop por todos os casos de teste
for _ in range(T):
    J = int(input())
    
    # Lengths
    L = []

    # Weights
    W = []

    # Ler entradas de um caso de teste
    for j in range(J):
        l, w = list(map(lambda x: int(x), input().split(' ')))

        L.append(l)
        W.append(w)

    # Array com as razoes de prioridade de cada job
    ratios = [(j, W[j]/L[j]) for j in range(J)]
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)

    w = 0
    # Iterando por todos os jobs ordenados por prioridade
    #   para somar a perda total
    for j, ratio in ratios:
        w += L[j] * sum(W)
        W[j] = 0

    print(w)


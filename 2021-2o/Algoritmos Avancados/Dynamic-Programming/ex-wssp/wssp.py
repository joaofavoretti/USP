import numpy as np

def wsspREC(i, w):
    if (MEMO[i][w] != -1): return MEMO[i][w]

    if (P[i] > w): 
        MEMO[i][w] = wsspREC(i-1, w)
    else:
        MEMO[i][w] = max(P[i] + wsspREC(i - 1, w - P[i]), wsspREC(i - 1, w))

    return MEMO[i][w]


W = int(input())
N = int(input())

MEMO = [[-1 for j in range(W + 1)] for i in range(N + 1)]

print(N, W)
print(MEMO)

P = list(map(int, input().split()))
P.sort()

for j in range(W + 1):
    MEMO[0][j] = 0

print(np.array(MEMO))
print(wsspREC(N, W))
print(np.array(MEMO))
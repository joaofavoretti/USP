# Python

def wispPD():
    for i in range(1, N + 1):
        MEMO[i] = max(V[i] + MEMO[P[i]], MEMO[i - 1])

    return MEMO[N]

def wispREC(i):
    if MEMO[i] != -1:
        return MEMO[i];

    MEMO[i] = max (V[i] + wispREC(P[i]), wispREC(i - 1))

    return MEMO[i]

N = int(input())
V = list(map(int, input().split()))
P = list(map(int, input().split()))

MEMO = [-1] * (N + 1)
MEMO[0] = 0
print(wispREC(N))

MEMO = [-1] * (N + 1)
MEMO[0] = 0
print(wispPD())
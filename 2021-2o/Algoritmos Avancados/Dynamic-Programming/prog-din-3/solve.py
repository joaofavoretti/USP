
"""
4
2 3 4 19 => 28 / 2 = 14
"""


def opt(i, w):

    if (MEMO[i][int(w * 10)] != -1):
        return MEMO[i][int(w * 10)]

    if (V[i] > w):
        MEMO[i][int(w * 10)] = opt(i - 1, w)
    else:
        MEMO[i][int(w * 10)] = max(
            V[i] + opt(i - 1, w - V[i]),
            opt(i - 1, w)
        )

    return MEMO[i][int(w * 10)]

n = int(input())

for _ in range(n):
    m = int(input())
    V = [0] + list(map(int, input().split()))
    S = sum(V)
    
    MEMO = [[-1 for j in range(S * 10 + 1)] for i in range(m + 1)]

    for j in range(S * 10 + 1):
        MEMO[0][j] = 0

    print(S - 2 * opt(m, S / 2))
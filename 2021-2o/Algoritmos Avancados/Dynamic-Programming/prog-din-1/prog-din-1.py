import sys

MAX = 10000

def solve(t):
    for j in range(1, t + 1):

        if j >= n and MEMO[j - n] != -1:
            MEMO[j] = max(MEMO[j], MEMO[j - n] + 1)

        if j >= m and MEMO[j - m] != -1:
            MEMO[j] = max(MEMO[j], MEMO[j - m] + 1)

    if MEMO[t] != -1:
        return f'{MEMO[t]}'
    
    for i in range(t, -1, -1):
        if MEMO[i] != -1:
            return f'{MEMO[i]} {t - i}'

while(True):
    try:
        MEMO = [-1] * MAX

        n, m, t = list(map(int, input().split()))

        MEMO[0] = 0

        print(solve(t))

    except EOFError: break
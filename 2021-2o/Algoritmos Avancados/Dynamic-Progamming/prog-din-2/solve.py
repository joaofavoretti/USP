import sys

MAX = 1000001
players = ['Stan', 'Ollie']

def solve(t):
    for j in range(2, t + 1):
        MEMO[j] = 1
        for i in range(m):
            if j >= stones[i] and MEMO[j - stones[i]] == 1:
                MEMO[j] = 0
                break

    return MEMO[t]

while(True):
    try:
        MEMO = [1] * MAX

        entry = list(map(int, input().split()))
        n = entry[0]
        m = entry[1]
        stones = entry[2:]

        MEMO[1] = 0

        print(MEMO[:n + 1])
        print(f'{players[solve(n)]} wins')
        print(MEMO[:n + 1])

    except EOFError: break
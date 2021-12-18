from collections import deque

N = int(input())

s = deque()

for _ in range(N):

    num = int(input())

    s = deque()

    for j in range(num // 2, 1, -1):
        div = False
        if num % j == 0 and j <= 9 and num // j <= 9:
            div = True
            s.append(j)
            s.append(num // j)

    if num < 10:
        print(num)
        continue

    if not div:
        print('-1')
        continue

    while s:
        print(s.pop(), end='')

    print()


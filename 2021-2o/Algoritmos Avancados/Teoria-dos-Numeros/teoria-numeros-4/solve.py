
def mdc(a, b):
    c = 0
    while a != 0:
        c = a
        a = b % a
        b = c
    return b

def mmc(a, b):
    g = mdc(a, b)
    if g == 0: return 0
    return a / g * b

T = int(input())
for _ in range(T):
    G, L = map(int, input().split())

    if L % G != 0: 
        print(-1)
        continue

    b = mdc(L, G)
    a = L / b * G
    if (a > b): print(int(b), int(a))
    else: print(int(a), int(b))
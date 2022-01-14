# Referencia para o algoritmo KMP: https://www.youtube.com/watch?v=GTJr8OvyEVQ

def search(text, patt, LPS):
    i = 0
    j = 0
    while i < len(text):
        if text[i] == patt[j]:
            i = i + 1
            j = j + 1
            if (j == len(patt)):
                return True
        else:
            if j == 0:
                i = i + 1
            else:
                j = LPS[j - 1]
    return False


def generateLPS(patt):
    LPS = [0] * len(patt)
    i = 0
    j = 1
    while j < len(patt):
        if patt[j] == patt[i]:
            LPS[j] = i + 1
            i = i + 1
            j = j + 1
        else:
            if i == 0:
                LPS[j] = 0
                j = j + 1
            else:
                i = LPS[i - 1]

    return LPS

# Unitary tests code
# T = input()
# P = input()
# lps = generateLPS(P)
# print(lps)
# if search(T, P, lps): print('Found')
# else: print("Not found")

# Run for each test case
k = int(input())
for _ in range(k):
    S = input().strip()
    q = int(input())
    for _ in range(q):
        T = input().strip()
        lps = generateLPS(T)
        if search(S, T, lps):
            print("y")
        else: print('n')

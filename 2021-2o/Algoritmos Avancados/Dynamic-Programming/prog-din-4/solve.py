# Indices
PRICE = 0
WEIGHT = 1

# Objects Array
MAX_N = 1000 + 1
MAX_P = 100 + 1
MAX_W = 30 + 1
OBJECTS = [[0, 0]] * MAX_N

# People array
MAX_G = 100 + 1
MAX_MW = 30 + 1
PEOPLE = [0] * MAX_G

MEMO = [0] * MAX_MW


T = int(input())

for _ in range(T):

    N = int(input())

    OBJECTS = [[0, 0]] * N
    MEMO = [0] * MAX_MW
    PEOPLE = [0] * MAX_G

    for i in range(N):
        p, w = input().split()
        OBJECTS[i] = [int(w), int(p)]

    G = int(input())

    for i in range(G):
        PEOPLE[i] = int(input())

    OBJECTS.sort()

    for i in range(N):
        itemWeight = OBJECTS[i][0]
        itemPrice = OBJECTS[i][1]
        
        for j in range(30, itemWeight - 1, -1):
            if itemPrice + MEMO[j - itemWeight] > MEMO[j]:
                MEMO[j] = itemPrice + MEMO[j - itemWeight]

    print(sum([MEMO[p] for p in PEOPLE]))


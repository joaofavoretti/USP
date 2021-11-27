
def findParent(u):
    if parent[u] == u:
        return u
    parent[u] = findParent(parent[u])
    return parent[u]

while(True):
    S, C = list(map(int, input().split()))
    
    if S == 0 and C == 0: break

    city = {}
    edges = []
    parent = {}
    # Edge = (u, v, w)

    for s in range(S):
        city[input().rstrip()] = s
        parent[s] = s

    for c in range(C):
        s1, s2, w = input().split()
        edges.append((int(w), city[s1], city[s2]))

    start = input()

    edges.sort()

    total = 0

    nOfConnections = 1
    for i in range(C):
        w, u, v = edges[i]
        
        parentU = findParent(u)
        parentV = findParent(v)

        if parentU != parentV:
            total += w
            parent[parentU] = parentV
            nOfConnections += 1

    if (nOfConnections == S):
        print(total)
    else: print("Impossible")


    

# Uva p820: Internet Bandwith

from queue import Queue



def calc_augmented(s, t, minEdge):
    global flow, parent

    if (t == s):
        flow = minEdge

    elif (parent[t] != -1):
        calc_augmented (s, parent[t], min(minEdge, graph[parent[t]][t]))
        graph[parent[t]][t] -= flow
        graph[t][parent[t]] += flow

test_cases = 0

while(True):
    N = int(input())
    test_cases += 1

    if N == 0: break

    print(f"Network {test_cases}")

    S, T, C = list(map(int, input().split()))
    
    # Usando os vertices 0-started
    S -= 1
    T -= 1

    graph = [[0 for _ in range(N)] for _ in range(N)]

    for c in range(C):
        u, v, w = list(map(int, input().split()))
        u -= 1
        v -= 1
        graph[u][v] += w
        graph[v][u] += w

    maxFlow = 0

    while(True):
        flow = 0
        dist = [1e7] * N
        dist[S] = 0
        q = Queue()
        q.put(S)
        parent = [-1] * N

        while (not q.empty()):
            k = q.get()
            if (k == T): break
            for i in range(N):
                if (graph[k][i] > 0 and dist[i] == 1e7):
                    dist[i] = dist[k] + 1
                    parent[i] = k
                    q.put(i)
        calc_augmented(S, T, 1e7)
        if flow == 0: break
        maxFlow += flow

    print(f'The bandwidth is {maxFlow}.\n')

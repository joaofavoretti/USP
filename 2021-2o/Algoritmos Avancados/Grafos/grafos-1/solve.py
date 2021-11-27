
from queue import Queue

# Declare variables
case_test = 1
edges = {}
has_in_edges = set()
vert = set()
self_connected_vert = False
num_edges = 0

def is_single_component():
    visitados = set()
    q = Queue()

    first_vert = -1
    a = 0
    # Find first vertice
    for vertice in vert:
        if vertice not in has_in_edges:
            first_vert = vertice
            a += 1

    if a != 1: return False

    visitados.add(first_vert)
    q.put(first_vert)

    while(q.empty() == False):
        k = q.get()

        if k in edges:
            for edge in edges[k]:
                if edge not in visitados:
                    visitados.add(edge)
                    q.put(edge)

    return len(visitados) == len(vert)

def solve():
    if len(vert) == 0:
        print(f"Case {case_test} is a tree.")
        return

    if self_connected_vert:
        print(f"Case {case_test} is not a tree.")
        return

    if len(vert) != num_edges + 1:
        print(f"Case {case_test} is not a tree.")
        return

    single_component = is_single_component()

    if single_component:
        print(f"Case {case_test} is a tree.")
        return

    if not single_component:
        print(f"Case {case_test} is not a tree.")
        return




while(True):
    u, v = list(map(int, input().split()))
    
    if u == 0 and v == 0:
        solve()

        # Reset variables
        edges = {}
        in_edges = {}
        vert = set()
        self_connected_vert = False
        num_edges = 0

        case_test += 1

        continue

    if u < 0 and v < 0: break

    vert.add(u)
    vert.add(v)

    if u == v:
        self_connected_vert = True
        continue

    num_edges += 1

    if u in edges:
        edges[u].append(v)
    else:
        edges[u] = [v]

    if v not in has_in_edges:
        has_in_edges.add(v)

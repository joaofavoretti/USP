"""
Playing the Wheels
Backtracking Algorithm (Using BFS)
author: Joao Pedro Favoretti
"""
from collections import deque
import heapq

directions = [[1, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, -1, 0, 0], 
        [0, 0, 1, 0], [0, 0, -1, 0], [0, 0, 0, 1], [0, 0, 0, -1]]

NUM_COORDS = 10000 # 10 x 10 x 10 x 10

walls = []

# A*
pqueue = []
visited = set() # Posicoes já visitadas
manh_dist = []

# BFS
queue = []
distances = []
discovered = []

# Modo de usar listas como tabelas hashes
def makeint(a, b, c, d):
    return d + c*10 + b*100 + a*1000

def a_star(current_pos, final_pos):
    global pqueue, visited

    fill_manh_dist(final_pos)

    distances = [-1] * NUM_COORDS

    heapq.heappush(pqueue, (0 + manh_dist[makeint(*current_pos)], makeint(*current_pos)))
    distances[makeint(*current_pos)] = 0

    while pqueue:
        cur_pos = heapq.heappop(pqueue)[1]
        cur_pos_distance = distances[cur_pos]

        if cur_pos == final_pos:
            return cur_pos_distance

        a_star_add_next_moves(cur_pos, cur_pos_distance)

        visited.add(cur_pos)

def fill_manh_dist(final_pos):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    manh_dist[makeint(i, j, k, l)] = abs(i - final_pos[0])
                    + abs(j - final_pos[1])
                    + abs(k - final_pos[2])
                    + abs(l - final_pos[3])

def a_star_add_next_moves(cur_dis, cur_pos_dis):
    global pqueue

    for pos in directions:
        # Soma vetorial cur_pos e pos
        next_pos = list(map(sum, zip(cur_dis, pos)))
    
        # Lembrar de modificar a coordenada já existente se tiver menor distancia
        if coord_valid(next_pos):
            # Não visitado
            if distances[makeint(*next_pos)] == -1:
                distances[makeint(*next_pos)] = cur_pos_dis + 1
    
                heapq.heappush(pqueue, (distances[makeint(*next_pos)] + manh_dist[makeint(*current_pos)], makeint(*current_pos)))

            # Já visitado, mas com menor distancia
            elif distances[makeint(*next_pos)] < cur_pos_dis + 1:
                # TODO: Algoritmo O(n), margem para melhorar
                pqueue.remove((distances[makeint(*next_pos)] + manh_dist[makeint(*next_pos)], makeint(*next_pos)))
                heapq.heapify(pqueue)
                
                distances[makeint(*next_pos)] = cur_pos_dis + 1

                heapq.heappush(pqueue, (distances[makeint(*next_pos)] + manh_dist[makeint(*current_pos)], makeint(*current_pos)))

            # Já tem distancia menor, não precisa adicionar
            else: continue 

def coord_valid(pos):
    not_wall = makeint(*pos) not in walls
    not_visited = makeint(*pos) not in visited
    not_out_of_scope = True
    for coord in pos:
        if coord > 9 or coord < 0:
            not_out_of_scope = False

    return not_wall and not_visited and not_out_of_scope 


def valid_next_pos(pos):
    not_wall = makeint(*pos) not in walls
    not_inserted = not discovered[makeint(*pos)]
    not_out_of_scope = True
    for coord in pos:
        if coord > 9 or coord < 0:
            not_out_of_scope = False

    return not_wall and not_inserted and not_out_of_scope 

def add_next_moves(cur_pos, cur_pos_dis):
    for pos in directions:
        # Soma vetorial current_pos e pos ()
        next_pos = list(map(sum, zip(cur_pos, pos)))
        
        # Adiciona novo movimento se for valido
        if valid_next_pos(next_pos):
            queue.append(next_pos)
            distances[makeint(*next_pos)] = cur_pos_dis + 1
            discovered[makeint(*next_pos)] = True

def bfs(current_pos, final_pos): 
    global queue, distances, discovered
 
    queue = deque([current_pos])
    distances = [-1] * NUM_COORDS
    discovered = [False] * NUM_COORDS

    distances[makeint(*current_pos)] = 0
    discovered[makeint(*current_pos)] = True

    while queue:
        cur_pos = queue.popleft()
        cur_pos_dis = distances[makeint(*cur_pos)] 

        if cur_pos == final_pos:
            return cur_pos_dis

        add_next_moves(cur_pos, cur_pos_dis)

    return -1 

N = int(input())

for test_case in range(N):

    s =  list(map(lambda x: int(x), input().split()))   # Read start coordinate
    f =  list(map(lambda x: int(x), input().split()))   # Read final coordinate

    walls = []
    n = int(input())
    for _ in range(n):
        wall = list(map(lambda x: int(x), input().split()))
        walls.append(makeint(*wall))
    walls = set(walls)

    print(bfs(s, f))

    # Lidar com a linha em branco entre as entradas (GOP)
    try: input()
    except: pass


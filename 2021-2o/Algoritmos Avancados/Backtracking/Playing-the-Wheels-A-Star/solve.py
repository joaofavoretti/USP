"""
Playing the Wheels
Backtracking Algorithm (Using BFS)
author: Joao Pedro Favoretti
"""
from collections import deque
import numpy as np
import heapq

directions = [[1, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, -1, 0, 0], 
        [0, 0, 1, 0], [0, 0, -1, 0], [0, 0, 0, 1], [0, 0, 0, -1]]

NUM_COORDS = 10000 # 10 x 10 x 10 x 10

walls = []

# A*
pqueue = []
visited = set() # Posicoes já visitadas
manh_dist = []
distances = []

# BFS
queue = []
distances = []
discovered = []

# Modo de usar listas como tabelas hashes
def makeint(a, b, c, d):
    return d + c*10 + b*100 + a*1000

# Passagem de volta para vetor
def makevec(a):
    return [a % 10000 // 1000, a % 1000 // 100, a % 100 // 10, a % 10]

def minimum_distance_a_star(current_pos, final_pos):
    global pqueue, visited, manh_dist, distances

    visited = set()
    pqueue = []
    manh_dist = [-1] * NUM_COORDS
    distances = [-1] * NUM_COORDS

    fill_manh_dist(final_pos)

    heapq.heappush(pqueue, (0 + manh_dist[makeint(*current_pos)], makeint(*current_pos)))
    distances[makeint(*current_pos)] = 0

    while pqueue:
        cur_pos = heapq.heappop(pqueue)[1]
        cur_pos_distance = distances[cur_pos]

        if makevec(cur_pos) == final_pos:
            return cur_pos_distance

        add_next_moves_a_star(cur_pos, cur_pos_distance)

        visited.add(cur_pos)
    
    return -1

def fill_manh_dist(final_pos):
    global pqueue, visited, manh_dist, distances

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    manh_dist[makeint(i, j, k, l)] = abs(i - final_pos[0]) + abs(j - final_pos[1]) + abs(k - final_pos[2]) + abs(l - final_pos[3])

def add_next_moves_a_star(cur_pos, cur_pos_dis):
    global pqueue, visited, manh_dist, distances

    for pos in directions:
        # Soma vetorial cur_pos e pos
        next_pos = list(map(sum, zip(makevec(cur_pos), pos)))

        if coord_valid(next_pos):
            # Não visitado
            if distances[makeint(*next_pos)] == -1:
                distances[makeint(*next_pos)] = cur_pos_dis + 1
    
                heapq.heappush(pqueue, (distances[makeint(*next_pos)] + manh_dist[makeint(*next_pos)], makeint(*next_pos)))

            # Já visitado, mas com menor distancia
            elif distances[makeint(*next_pos)] > (cur_pos_dis + 1) and makeint(*next_pos) not in visited:
                remove_from_pqueue(makeint(*next_pos))
                
                distances[makeint(*next_pos)] = cur_pos_dis + 1

                heapq.heappush(pqueue, (distances[makeint(*next_pos)] + manh_dist[makeint(*next_pos)], makeint(*next_pos)))

            # Já tem distancia menor, não precisa adicionar
            else: continue

def remove_from_pqueue(pos):
    global pqueue
    for h, coord in pqueue:
        if coord == pos:
            pqueue.remove((h, coord))
            heapq.heapify(pqueue)
            break

def coord_valid(pos):
    not_wall = makeint(*pos) not in walls
    not_visited = makeint(*pos) not in visited
    not_out_of_scope = True
    for coord in pos:
        if coord > 9 or coord < 0:
            not_out_of_scope = False

    return not_wall and not_visited and not_out_of_scope 


"""
 Inicio do programa
"""

N = int(input())

for test_case in range(N):
    s =  list(map(lambda x: int(x), input().split()))   # Start
    f =  list(map(lambda x: int(x), input().split()))   # Finish

    walls = []
    n = int(input())
    for _ in range(n):
        wall = list(map(lambda x: int(x), input().split()))
        walls.append(makeint(*wall))
    walls = set(walls)

    print(minimum_distance_a_star(s, f))

    # Lidar com a linha em branco entre as entradas (GOP)
    try: input()
    except: pass


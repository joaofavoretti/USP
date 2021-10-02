"""
Playing the Wheels
Backtracking Algorithm (Using BFS)
author: Joao Pedro Favoretti
"""
from collections import deque

cursor_positions = [[1, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, -1, 0, 0], 
        [0, 0, 1, 0], [0, 0, -1, 0], [0, 0, 0, 1], [0, 0, 0, -1]]

NUM_COORDS = 100000

walls = []
# Transformar em deque
next_mov = deque()
distances = []
discovered = []

def valid_next_pos(pos):
    not_wall = make_int(*pos) not in walls
    not_inserted = not discovered[make_int(*pos)]
    not_out_of_scope = True
    for coord in pos:
        if coord > 9 or coord < 0:
            not_out_of_scope = False

    return not_wall and not_inserted and not_out_of_scope 

def add_next_moves(cur_pos, cur_pos_dis):
    for pos in cursor_positions:
        # Soma vetorial current_pos e pos ()
        next_pos = list(map(sum, zip(cur_pos, pos)))
        
        # Adiciona novo movimento se for valido
        if valid_next_pos(next_pos):
            next_mov.append(next_pos)
            distances[make_int(*next_pos)] = cur_pos_dis + 1
            discovered[make_int(*next_pos)] = True

def bfs(current_pos, final_pos): 
    global next_mov, distances, discovered
 
    next_mov = deque([current_pos])
    distances = [-1] * NUM_COORDS
    discovered = [False] * NUM_COORDS

    distances[make_int(*current_pos)] = 0
    discovered[make_int(*current_pos)] = True

    while next_mov:
        cur_pos = next_mov.popleft()
        cur_pos_dis = distances[make_int(*cur_pos)] 

        if cur_pos == final_pos:
            return cur_pos_dis

        add_next_moves(cur_pos, cur_pos_dis)

    return -1 

# Modo de usar listas como tabelas hashes
def make_int(a, b, c, d):
    return d + c*10 + b*100 + a*1000

N = int(input())

for test_case in range(N):

    c =  list(map(lambda x: int(x), input().split()))
    f =  list(map(lambda x: int(x), input().split())) 

    walls = []
    n = int(input())
    for _ in range(n):
        wall =  list(map(lambda x: int(x), input().split()))
        walls.append(make_int(*wall)) 
    walls = set(walls)

    print(bfs(c, f))

    # Lidar com a linha em branco entre as entradas (GOP)
    try: input()
    except: pass


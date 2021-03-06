"""
N Queen Problem
Backtracking Algorithm
author: Joao Pedro Favoretti
"""
import numpy as np

NROWS = 8
NCOLS = 8

def coord_in_board(row, col):
    if row < 0 or col < 0 or row >= NROWS or col >= NCOLS: return False

    return True

# Checar todo o tabuleiro
def has_conflict(board, crow, ccol):
    # Checar linhas
    if sum(board[crow]) > 1: return True
 
    # Checar coluna
    if sum([board[row][ccol] for row in range(NROWS)]) > 1: return True

    # Checa o 2o e 4o quadrantefor row, col in zip(range(-NROWS, NROWS, 1), range(-NCOLS, NCOLS, 1)):
    sum_diag = 0
    for row, col in zip(range(0, NROWS, 1), range(0, NCOLS, 1)):
        r = row
        c = col + (ccol - crow)

        # Checa coordenada valida
        if not coord_in_board(r, c): continue 
        
        sum_diag += board[r][c]
       
        if sum_diag > 1: return True 
 
    # Checa o 1o e 3o quadrante
    sum_diag = 0
    for row, col in zip(range(NROWS-1, -1, -1), range(0, NCOLS, 1)):
        r = row
        c = col + (ccol + crow - NCOLS + 1)

        # Checa coordenada valida
        if not coord_in_board(r, c): continue 
        
        sum_diag += board[r][c]

        if sum_diag > 1: return True
    
    return False

def backtracking(board_val, board, n_row, values):
    if (n_row >= NROWS):
        # Calcular o valor do tabuleiro encontrado.
        board_value = sum([sum([value * col for value, col in zip(board_val[row], board[row])]) for row in range(NROWS)])

        # Adicionar na lista de valores dos tabuleiros formados
        values.append(board_value)

        return
    # Colocar uma rainha em uma posicao
    for col in range(NCOLS):
        board[n_row][col] = 1
        
        # Checar se existe conflito
        if not has_conflict(board, n_row, col):
            # Se nao existir, passa para a proxima linha    
            backtracking(board_val, board, n_row + 1, values)
 
        # Se existir, volta e tenta outra posicao
        board[n_row][col] = 0

def main():
    K = int(input())

    for k in range(K):
        chessboard_value = []
        chessboard = [[0 for _ in range(NCOLS)] for _ in range(NROWS)]

        for row in range(NROWS):
            r = list(map(lambda x: int(x), input().split()))
            chessboard_value.append(r)

        # Array de valores dos tabuleiros formados
        values = [] 
        backtracking(chessboard_value, chessboard, 0, values)
        print(f'{max(values): >5}')
        # print('{0}'.format(message=max(values))

if __name__ == '__main__':
    main()

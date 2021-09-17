"""
Proposito do programa:
    Mostrar todas as combinacoes de uma lista de char
    Baseado no vetor {a, b, c}
    {a, b, c} -> {a, b, c}, {a, c, b}, {b, a, c}, {b, c, a}, {c, a, b}, {c, b, a}
"""
SIZE = 3

def backtracking(vec, pos):
    if pos == SIZE - 1:
        print(vec[0], vec[1], vec[2])
        return

    for i in range(pos, SIZE, 1):
        vec[pos], vec[i] = vec[i], vec[pos]     # Swap the index to choose the others
        
        backtracking(vec, pos + 1)
    
        vec[pos], vec[i] = vec[i], vec[pos]     # Swap the index to choose the others


def main():
    global SIZE

    vec = ['a', 'b', 'c', 'd']
    SIZE = len(vec)
    
    backtracking(vec, 0)


if __name__ == '__main__':
    main()


# j = ULTIMO EXCLUSIVO
def solve(a, i, j):
    if (j - i == 1):
        return min(a)[0]
    
    if (j - i <= 0):
        return 0

    min_val, min_index = min(a)
    
    s_current = min_val * (j - i)

    if (min_index - i < j - min_index + 1):
        s_min = set(filter(lambda x: x[1] < min_index, a))

        a.difference_update(s_min)

        a.remove((min_val, min_index))

        return max([solve(s_min, i, min_index), solve(a, min_index + 1, j), s_current])
    
    s_min = set(filter(lambda x: x[1] > min_index, a))

    a.difference_update(s_min)

    a.remove((min_val, min_index))

    return max([solve(a, i, min_index), solve(s_min, min_index + 1, j), s_current])


def main():
    n = int(input())
    a = set(map(lambda x : (int(x[1]), x[0]), enumerate(input().split())))
    print(solve(a, 0, n))

main()

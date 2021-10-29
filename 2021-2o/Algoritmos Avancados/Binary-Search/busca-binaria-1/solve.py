""" The Monkey and the Oiled Bamboo """

MIN_K = 0
MAX_K = 10000000

def enough(k, rungs):
    K = k

    for i in range(len(rungs) - 1):
        if rungs[i] + K < rungs[i + 1]:
            return False
        elif rungs[i] + K == rungs[i + 1]:
            K -= 1

    return True

def find_k(min, max, rungs):
    if max - min <= 1:
        return max

    mid = (min + max) // 2

    if enough(mid, rungs):
        return find_k(min, mid, rungs)
    else:
        return find_k(mid, max, rungs)

def main():
    T = int(input())
    
    # Test cases
    for i in range(T):
        N = int(input())
        rungs = [0] + list(map(int, input().split()))

        print(f'Case {i + 1}: {find_k(MIN_K, MAX_K, rungs)}')

main()

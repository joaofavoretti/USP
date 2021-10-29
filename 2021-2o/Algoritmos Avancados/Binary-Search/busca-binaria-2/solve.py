"""  """

MIN_CAPACITY = 0
MAX_CAPACITY = 1000000

def enough(capacity, n_containers, vessels):
    current_vol = 0
    i = 1

    for vessel in vessels:
        if vessel > capacity: return False

        if current_vol + vessel > capacity:
            i += 1
            current_vol = 0
        
        if i > n_containers: return False

        current_vol += vessel

    return True


def find_k(min, max, n_containers, vessels):
    if max - min <= 1:
        return max

    mid = (min + max) // 2

    if enough(mid, n_containers, vessels):
        return find_k(min, mid, n_containers, vessels)
    else:
        return find_k(mid, max, n_containers, vessels)

while(True):
    try:
        n_vessels, n_containers = tuple(map(int, input().split()))
        vessels = list(map(int, input().split()))

        print(find_k(MIN_CAPACITY, MAX_CAPACITY, n_containers, vessels))
    except EOFError: break

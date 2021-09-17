
class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function


"""
 'segments(pt1, pt2)' retorna um array de 100 elementos numpy de pt1 a pt2
 pt1 e pt2 devem ser arrays com as coordenadas dos pontos
 ex: segments([0.5, 1], [3.5, 3])

"""
def segments(pt1, pt2):
    if not isinstance(pt1, list) or not isinstance(pt2, list):
        print("Error: pt1 or pt2 are not lists")
        return

    if len(pt1) != len(pt2):
        print('Error: pt1 has different length then pt2')
        return

    steps = 100
    vec_length = int(len(pt1))   # Equals len pt2

    r = [[(a/steps) * pt1[c] + (1 - (a/steps)) * pt2[c] for c in range(0, vec_length)] for a in range(0, steps)]
    
    return r

def list_dot(u, v):
    if len(u) != len(v):
        return []

    return sum ([u[i] * v[i] for i in range(0, len(u))])

def dot_product_list(haystack, needle):
    if len(haystack) < len(needle):
        return []

    n = len(needle)
    h = len(haystack)

    return [list_dot(haystack[i: i + n], needle)  for i in range(0, h - n + 1)]

needle = [1, -1, 1, 1, -1, 1]
haystack = [1, -1, 1, 1, 1, -1, 1, 1, 1]
print(dot_product_list(haystack, needle))

"""
author: Joao Pedro Favoretti
"""

def mergesort(vec, start, end):
    if end <= start + 1:
        return 0

    mid = start + (end - start) // 2

    return mergesort(vec, start, mid) + mergesort(vec, mid, end) + merge(vec, start, mid, end)

def merge(vec, start, mid, end):
    i, j, count = 0, 0, 0
    left, right = vec[start:mid], vec[mid:end]
    k = start

    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            vec[k] = left[i]
            i += 1

        else:
            vec[k] = right[j]
            j += 1
            count += ((mid - start) - i)
        
        k += 1

    while start + i < mid:
        vec[k] = left[i]
        i += 1
        k += 1

    while mid + j < end:
        vec[k] = right[j]
        j += 1
        k += 1

    return count

def main():
    while True:
        n = int(input())

        if n == 0: break

        a = [ int(input()) for i in range(n)]

        print(mergesort(a, 0, n))

main()

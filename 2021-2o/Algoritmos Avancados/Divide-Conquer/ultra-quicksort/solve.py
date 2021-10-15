def mergesort(vec, start, end):
    if end - start <= 1:
        return 0

    mid = start + (end - start) // 2

    return mergesort(vec, start, mid) + mergesort(vec, mid, end) + merge(vec, start, mid, end)

def merge(vec, start, mid, end):
    i, j = 0, 0
    count = 0
    left, right = vec[start:mid], vec[mid:end]

    for k in range(start, end):
        if i == mid - start:
            vec[k] = right[j]
            j += 1

        elif j == end - mid:
            vec[k] = left[i]
            i += 1

        else:
            if left[i] <= right[j]:
                vec[k] = left[i]
                i += 1
            else:
                vec[k] = right[j]
                j += 1
                count += ((mid - start) - i)

    return count

def main():
    while True:
        n = int(input())

        if n == 0: break

        a = [ int(input()) for i in range(n)]

        print(mergesort(a, 0, n))  

if __name__ == '__main__':
    main()

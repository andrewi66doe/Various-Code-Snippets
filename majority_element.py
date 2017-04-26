import math
import time


def majority_element_naive(A):
    element_counts = {}
    for element in A:
        if element in element_counts.keys():
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    return max(element_counts, key=lambda x: element_counts[x])


def majority_element_dc(A):
    n = len(A)

    if n == 1:
        return A[0]

    k = math.floor(n / 2)

    elem_l = majority_element_dc(A[:k])
    elem_r = majority_element_dc(A[k:])

    if elem_l == elem_r:
        return elem_l

    count_l = A.count(elem_l)
    count_r = A.count(elem_r)

    if count_l >= math.floor(n / 2):
        return elem_l
    elif count_r >= math.floor(n / 2):
        return elem_r
    else:
        return None


def tricky():
    w1 = ['b', 'l', 'a', 'c', 'k', 's', 'm', 'i', 't', 'h']
    w2 = ['p', 'o', 'w', 'd', 'e', 'r', 'y']

    id = '1293538'

    A = [' ' for _ in range(10)]
    B = [' ' for _ in range(7)]

    for i in range(9):
        A[i] = w1[i]
    for j in range(6):
        B[j] = w2[j]
        k = id[j]
        A[int(k)] = B[j]

    return A


if __name__ == "__main__":
    A = [3, 3, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 4, 3, 3, 3, 3]
    a = time.time()
    print(majority_element_naive(A))
    b = time.time()
    print(b-a)

    a = time.time()
    print(majority_element_dc(A))
    b = time.time()
    print(b-a)


    print(tricky())

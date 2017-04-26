def merge_sort(arr):

    if len(arr) == 1:
        return arr
    l = len(arr) // 2

    left = arr[:l]
    right = arr[l:]

    left = merge_sort(left)     # T(n/2)
    right = merge_sort(right)   # T(n/2)

    return merge(left, right)   # O(n) complexity

# Complete complexity is T(n) = 2T(n/2) + O(n) which is O(nlog(n))


def merge(arr_l, arr_r):
    c = []

    while len(arr_l) > 0 and len(arr_r) > 0:
        if arr_l[0] > arr_r[0]:
            c.append(arr_r[0])
            del arr_r[0]
        else:
            c.append(arr_l[0])
            del arr_l[0]

    for elem in arr_l:
        c.append(elem)

    for elem in arr_r:
        c.append(elem)

    return c


if __name__ == "__main__":
    unsorted = [1, 3, 8, 7, 3, 4, 2, 12]

    print(merge_sort(unsorted))

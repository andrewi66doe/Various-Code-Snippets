
def exclusive_product_no_division(array):
    above = []
    below = []
    result = []

    i = 1

    for j, _ in enumerate(array):
        above.append(i)
        i *= array[j]

    i = 1
    j = len(array) - 1
    while j >= 0:
        below.append(i)
        i *= array[j]
        j -= 1
    below.reverse()

    for i, _ in enumerate(array):
        result.append(above[i] * below[i])

    return result


def exclusive_product(array):
    product = 1
    result = []

    for x in array:
        product *= x

    for x in array:
        result.append(product/x)

    return result


def recursive_power(x, n):
    if n == 0:
        return 1
    else:
        return x * recursive_power(x, n - 1)


def rec_power(x, n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return x * rec_power(x, n/2) * rec_power(x, n/2)
    else:
        return rec_power(x, n/2) * rec_power(x, n/2)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(exclusive_product([3, 4, 5, 6]))
    print(exclusive_product_no_division([3, 4, 5, 6]))

    for k in range(5):
        print(recursive_power(2, k))

    print(fib(5))

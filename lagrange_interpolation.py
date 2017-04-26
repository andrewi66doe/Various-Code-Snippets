import numpy


def lagrange_interpolation(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    polynomials = []

    for x_index, x in enumerate(x_values):
        # k != 0
        vals = [element for i, element in enumerate(x_values) if i != x_index]
        polynomial = numpy.poly1d(vals, True)
        print(polynomial)
        coeffecients = polynomial.coeffs
        constant = 1/numpy.prod(list(map(lambda val: x-val, vals)))
        polynomials.append((coeffecients, constant))

    scaled_polynomials = []

    for i, y in enumerate(y_values):
        coeffecients, constant = polynomials[i]

        scalar = (float(constant) * float(y))
        scaled_coefficients = map(lambda coefficient: coefficient * scalar,
                                  coeffecients)
        scaled_polynomials.append(list(scaled_coefficients))

        vectors = map(numpy.array, scaled_polynomials)
        final_coefficients = sum(vectors)

    return numpy.poly1d(final_coefficients)

if __name__ == "__main__":
    p = [(1, 1), (2, 4)]
    print(lagrange_interpolation(p))

def Romberg(f, startAt, endAt, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [startAt, endAt]

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param sectionAmount: The amount of section
    """
    f = lambdify(x, f)

    R = [[0 for _ in range(sectionAmount)] for _ in range(sectionAmount)]

    for i in range(sectionAmount):
        R[i][0] = Trapezoidal(f, startAt, endAt, 2 ** i)

        for j in range(i):
            R[i][j + 1] = (4 ** (j + 1) * R[i][j] - R[i - 1][j]) / (4 ** (j + 1) - 1)

    print(f'Sum of the area --> {int(R[-1][-1] * 10 ** 5) / 10 ** 5}')
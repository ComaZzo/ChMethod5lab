from math import log, sqrt

epsilon = 5 * 10 ** -7

a = 2
b = 3


def func(x: float) -> float:
    return 1 / (1 + sqrt(log(x)))


def simpson_method():
    n = 2
    for i in range(100):
        s = sqr_simpson(n)
        n *= 2
        s_next = sqr_simpson(n)
        if abs(s_next - s) < epsilon:
            print('Simpson method at {} step result:     {:.8f} | {} iteration'.format(n, s_next, i))
            break
    else:
        print('Simpson method not reached epsilon')


def trapezoid_method():
    n = 2
    for i in range(100):
        s = sqr_trapezoid(n)
        n *= 2
        s_next = sqr_trapezoid(n)
        if abs(s_next - s) < epsilon:
            print('Trapezoid method at {} step result:  {:.8f} | {} iteration'.format(n, s_next, i))
            break
    else:
        print('Trapezoid method not reached epsilon')


def sqr_simpson(n: int) -> float:
    h = (b - a) / n
    result_sqr = func(a) + func(b)

    for i in range(1, n):
        if i % 2 == 0:
            result_sqr += 2 * func(a + i * h)
        else:
            result_sqr += 4 * func(a + i * h)

    return result_sqr * h / 3


def sqr_trapezoid(n: int) -> float:
    h = (b - a) / n
    result_sqr = (func(a) + func(b)) / 2
    for i in range(1, n):
        result_sqr += func(a + i * h)
    return result_sqr * h


if __name__ == '__main__':
    simpson_method()
    trapezoid_method()

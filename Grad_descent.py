import math


def function(value: float):
    return math.sqrt(2 / math.pi) * math.exp(-(value**2))


def left_integral(func, N: int, lower: float, upper: float):
    step = (upper - lower) / N
    sum = 0
    for i in range(N - 1):
        sum += function(i * step) * step
    return sum


def right_integral(func, N: int, lower: float, upper: float):
    step = (upper - lower) / N
    sum = 0
    for i in range(1, N):
        sum += function(i * step) * step
    return sum


def integral(function, lower: float, upper: float, precision: float):
    N = 2
    left = precision
    right = 3 * left
    while abs(left - right) > precision:
        left = left_integral(function, N, lower, upper)
        right = right_integral(function, N, lower, upper)
        print(f'{N=}, {left=}, {right=}, {abs(left - right)}')
        N = 2 * N
    return (left + right) / 2


def ode(function, x: float, precision: float):
    pass


ode.lower = 0
ode.upper = 0
ode.x = 0


def derivative(x: float, function=function):
    return function(x) - 2 * x * math.exp(-x * x)


def full_function(x: float, precision: float, function=function):
    return integral(function, 0, x, precision) + math.exp(-x * x)


def gradient_descent(
    f, df, initial: float, lr: float, precision: float, max_iterations: int
):
    diff = 2 * precision
    ret = f(initial, precision, function)
    x = initial
    iter = 1
    while diff > precision and iter < max_iterations:
        i = 0
        while i < 2 * iter:
            x -= lr * df(x)
            i += 1
        value = f(x, precision)
        diff = abs(value - ret)

        iter += 1
        print(f'{iter=} {x=} {ret=} {value=} {diff=}')
        ret = value

    return ret


print(
    'result:',
    gradient_descent(
        full_function,
        derivative,
        1.0,  # initial point; should be chosen randomly between 0 and 100
        10,  # leaning rate
        0.000001,  # accuracy
        10000,  # max iterations
    ),
)

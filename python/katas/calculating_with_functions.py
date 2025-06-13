def zero(fn=None):
    return fn(0) if fn is not None else 0


def one(fn=None):
    return fn(1) if fn is not None else 1


def two(fn=None):
    return fn(2) if fn is not None else 2


def three(fn=None):
    return fn(3) if fn is not None else 3


def four(fn=None):
    return fn(4) if fn is not None else 4


def five(fn=None):
    return fn(5) if fn is not None else 5


def six(fn=None):
    return fn(6) if fn is not None else 6


def seven(fn=None):
    return fn(7) if fn is not None else 7


def eight(fn=None):
    return fn(8) if fn is not None else 8


def nine(fn=None):
    return fn(9) if fn is not None else 9


def plus(x: int = 0):
    return lambda n: n + x


def minus(x: int = 0):
    return lambda n: n - x


def times(x: int = 0):
    return lambda n: n * x


def divided_by(x: int = 0):
    return lambda n: int(n / x)


def test():
    print(two(times(two())))


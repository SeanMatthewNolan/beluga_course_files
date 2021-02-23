def func(x, y):
    z = x * y - 2
    return z


def func2(x, y, op='add'):
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    else:
        return None


def func3(x, y):
    a = 2

    def inner_func(z):
        return a * (x + y)*z

    a = 3

    return inner_func

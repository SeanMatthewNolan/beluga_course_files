# Structure in Python is given by whitespace

# Functions are defined with def
def func1(x, y):
    out = x + y
    return out


# Functions can take keyword argument
def func2(x, y, op='add'):
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    else:
        return None

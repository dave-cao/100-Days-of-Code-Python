def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 10))

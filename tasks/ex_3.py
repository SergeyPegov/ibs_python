
numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def f(x):
    return x > 50 and x % 2 != 0

print(list(filter(f,numbers)))



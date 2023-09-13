def fibonacci(n):
    a = 0
    b = 1
    c = 0
    i = n
    while i != 0:
        i = i - 1
        a = b
        b = c
        c = a + b
    return b

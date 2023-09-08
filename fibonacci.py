a = 0
b = 1
c = 0

# "How many numbers of the series:"
# FPS Assign(i, input("Enter n:"))
n = input("Enter n:")
i = int(n)
_step = 1

# block for computing the series:
while i != 0:

    print(f"Step: {_step} - {c}")

    i = i-1
    a = b
    b = c
    c = a + b
    _step = _step+1

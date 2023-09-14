from fibonacci_module import fibonacci

print("enter n")
inp = input()
n = int(inp)
l = fibonacci(n)
i = 0
print("the fibonacci series is:")
while i < len(l):
    print(l[i])
    i = i+1

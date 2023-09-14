from fibonacci_module import fibonacci

print("enter n")
inp = input()
n = int(inp)
l = fibonacci(n)
print("the fibonacci series is:")
# l = [0,1,1,2,3]
# for <individual> in <group>:
for e in l:
    print(e)
    if e == 3:
        break
    else:
        pass

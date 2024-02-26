def f(x):
    s = str(x)
    t = sum(int(i) for i in s)
    return x%t==0
print(f(5))
for n in range(467693, 467741):
    if f(n):
        print(n)

def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

print(f(13))
for n in range(907645, 907710):
    if f(n):
        print(n)

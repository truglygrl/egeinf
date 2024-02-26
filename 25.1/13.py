def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for n in range(2410000, 2410101):
    if f(n):
        print(n)
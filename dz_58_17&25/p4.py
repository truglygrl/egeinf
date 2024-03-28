def f(a):
    s = set()
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            s.add(i)
            s.add(a // i)
    return s


print(f(81))

for x in range(1523467, 4157813):
    if int(x**0.5) == x ** 0.5:
        if len(f(x)) == 3:
            print(x, max(f(x)))
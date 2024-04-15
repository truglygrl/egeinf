def f(n):
    s = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return list(s)
k = 0
for x in range(265980,265980*10000):
    if sum(f(x)) % 734 == 67:
        k += 1
        print(x)
    if k == 6:
        break
summ = 0

for n in range(10000, 12345):
    c = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            c.add(i)
            c.add(n//i)
        if len(c) > 5:
            break
    if len(c) == 2:
        print(c, n)
        summ += n

print(summ)
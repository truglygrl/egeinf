cnt = 0

for n in range(110000,250001):
    c = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            c.add(i)
            c.add(n//i)
    if len(c) == 5:
        cnt += 1
        print(c, n)

print(cnt)
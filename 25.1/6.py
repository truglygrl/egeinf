cnt = 0

for n in range(21514, 30102):
    c = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c.add(i)
            c.add(n//i)
    if len(c) == 3:
        cnt += 1
        print(c, n)

print(cnt)
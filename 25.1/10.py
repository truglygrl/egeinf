cnt = 0
a = []
for n in range(4301614, 4301718):
    c = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c.add(i)
            c.add(n//i)
    if len(c) == 0:
        cnt += 1
        print(n)

print(cnt)
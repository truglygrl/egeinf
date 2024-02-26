cnt = 0

for n in range(193136, 193224):
    c = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            c.add(i)
            c.add(n//i)
    if len(c) == 6:
        cnt += 1
        print(sorted(c)[-2], sorted(c)[-1])

print(cnt)

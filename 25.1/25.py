cnt = 0
for n in range(35798, 1000000):
    c = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            c.add(i)
            c.add(n// i)
        if len(c) > 5:
            break
    if len(c) == 5:
        print(n)
        cnt += 1
        if cnt == 5:
            break
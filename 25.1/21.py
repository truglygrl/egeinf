cnt = 0
for n in range(100100, 300101):
    c = set()
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            c.add(i)
            c.add(n // i)
    if len(c) == 4:
        cnt +=1
print(cnt)
a = set()
for n in range(123123, 345346):
    c = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            c += 1
    if c == 0:
        a.add(n)
print(min(sorted(a)), max(sorted(a)))
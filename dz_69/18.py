def f(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True



c = 0
a = [n for n in range(500000, 1500000+1)]
for x in range(len(a)-2):
    if f(a[x]) and f(a[x+2]):
        c += 1
print(c)
def sm(x):
    s = 0
    while x > 0:
        s += x % 10
        x = x // 10
    return s

c = set()

for i in range(1000001268, 19999999992, 2023):
    s = str(i)
    if (s[0] == '1') and (s[-1] == '1'):
        c.add(sm(i))
print(sorted(c))
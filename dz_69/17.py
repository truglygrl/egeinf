def f(a):
    s = set()
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            s.add(i)
            s.add(a // i)
    s = sorted(s)
    if len(s) != 4:
        return False
    if len(s) == 4:
        tc = [i for i in s if i % 2 == 0]
        tn = [i for i in s if i % 2 != 0]
        if len(tc) == len(tn) == 2:
            return True
ans = []
for x in range(90000, 147000+1):
    if f(x):
        ans.append(x)
print(len(ans), sum(ans))
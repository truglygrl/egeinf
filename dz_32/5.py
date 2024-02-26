ans = []
f = open('4__1n2ut.txt')
t = [int(i) for i in f]
for i in range(len(t)-2):
    a, b, c = sorted([int(x) for x in t[i:i+3]])
    if c**2 == a**2 + b**2:
        ans.append(c)
print(len(ans), sum(ans))
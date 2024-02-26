n = int(input())
a = []
for i in range(n):
    a.append(0.5**i)
print(*a, sep=', ')
f = open('27-4b__36tx5.txt')
n = int(f.readline())
s = 0
mr = [10**10]*5
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mr[d % 5] = min(mr[d % 5], d)

if s % 5 != 0:
    s -= mr[s % 5]
print(s)
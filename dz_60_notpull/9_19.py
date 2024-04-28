f = open('9_19')
n = 3000
max1 = 20000
c = 0
for i in range(n):
    a = sorted(list(map(int, f.readline().split())))
    tc = [x for x in a if x % 2 == 0]
    tn = [x for x in a if x % 2!= 0]
    if (sum(tc) > sum(tn)) and ((max(a) + min(a)) > max1):
        c += 1
print(c)
f = open('10_A__2rcu1.txt')
n = int(f.readline())
a = []
k = 148
c = 0
x = int(f.readline())
for i in range(n-1):
    x = int(f.readline())
    for j in a:
        if (x + j) % k == 0:
            c += 1
    a.append(x)
    if len(a) > 10:
        a.pop(0)
print(c)

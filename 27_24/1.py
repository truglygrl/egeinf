f = open('10_B__2rcu2.txt')
#f = open('10_A__2rcu1.txt')
n = int(f.readline())
a = [int(i) for i in f]
r = 0
k = 148
p = [0]
for i in range(n):
    for d in p:
        if (a[i] + d) % k == 0:
            r += 1
    p += [a[i]]
    if len(p) > 10:
        p.pop(0)
print(r)


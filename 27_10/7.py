f = open('7_B__2rcti.txt')
n = int(f.readline())
k = 177
c = 0
#a = [int(i) for i in f]
p = [0]*k

for i in range(n):
    x = int(f.readline())
    p[x % k] += 1
print(p)
for i in range(k):
    c += p[i]*(p[i]-1)//2
print(c)
"""for i in range(n-1):
    for j in range(i+1, n):
        if abs(a[j] - a[i]) % 177 == 0:
            c += 1
print(c)"""
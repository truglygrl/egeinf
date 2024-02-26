f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/3a.txt')
n = int(f.readline())
k = 91
p0 = [0]*k
p33 = [0]*k
for i in range(n):
    x = int(f.readline())
    if x > 33:
        p33[x%k] += 1
    else:
        p0[x%k] += 1
c = p33[0]*(p33[0]-1)//2

for i in range(1, k//2+1):
    c += p33[i]*p33[k-i]
    c += p0[i]*p33[k-i]
    c += p33[i]*p0[k-i]

print(c)
"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if (s%91 == 0) and ((a[i] > 33) or a[j] > 33):
            c += 1
print(c)"""
f = open('4_B__2rct7.txt')
k = 5
n = int(f.readline())
a = [int(i) for i in f]
m = s1 = mn = 1000000000
for i in range(n-k*2):
    m = min(a[i], m)
    s1 = min(s1, m+a[i+k])
    mn = min(mn, s1 + a[i+k*2])
print(mn)
f = open('4_A__2rct6.txt')
#f = open('4_B__2rct7.txt')
n = int(f.readline())
a = [int(i) for i in f]

m1 = m2 = mn = 10**10
for i in range(n-10):
    m1 = min(m1, a[i])
    m2 = min(m2, m1 + a[i+5])
    mn = min(m2 + a[i+10], mn)
print(mn)
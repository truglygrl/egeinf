f = open('6_B__2rctc.txt')
#f = open('6_A__2rctb.txt')

n = int(f.readline())
a = [int(i) for i in f]

m = mn = 10**10

for i in range(n-9):
    m = min(m, a[i])
    mn = min(m+a[i+9], mn)
print(mn)
f = open('8_B__1vjy7.txt')
#f = open('8_A__1vjy6.txt')
k = 4
#максимальное произведение двух показаний, кратное 6
n = int(f.readline())
a = [int(i) for i in f]
d = 6
p = [0]*6
mx = -1900000000000000000000
for i in range(n-k):
    p[a[i] % d] = max(p[a[i] % d], a[i])
    for pas in p:
        if (a[i+k]*pas) % 6 == 0:
            mx = max(mx, a[i+k]*pas)

print(mx, mx % 6)
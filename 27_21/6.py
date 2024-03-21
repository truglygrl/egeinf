"""ms = -100000000
k = 98
ms = -10000000000000
p = [-10000000000]*k
f = open('27B__tcf5.txt')
#f = open('27A__tcf4.txt')
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+1] % k) % k
    if p[t] > 0:
        ms = max(ms, a[i+1] + p[t])
        if ms == 19992:
            print(a[i+1], ms - a[i+1])
print(ms)


oo*(143+107)*2 + 0.22(95+19)*5/2 = 112,7
"""#Д,   Н,     Й,     А,    Л,      Е
#['00', '01', '010', '11', '100', '101']])

r = '0010100100111001'  #000 101 000 100 11 010 001
a = (int(r, 2))
print(a)
print(hex(a))
n = int(input())
m1 = m2 = m3 = m6 = mp = 0
x = int(input())
for i in range(n - 1):
    if x > m1:
        m1 = x
    if x > m2 and x % 2 == 0:
        m2 = x
    if x > m3 and x % 3 == 0:
        m3 = x
    if x > m6 and x % 6 == 0:
        m6 = x
    x = int(input())
    if (x * m1 > mp) and (x*m1 % 6 == 0) and (m1 > x):
        mp = x*m1
    if (x * m2 > mp) and (x*m2 % 6 == 0) and (m2 > x):
        mp = x*m2
    if (x * m3 > mp) and (x*m3 % 6 == 0) and (m3 > x):
        mp = x*m3
    if (x * m6 > mp) and (x*m6 % 6 == 0) and (m6 > x):
        mp = x*m6

print(mp)
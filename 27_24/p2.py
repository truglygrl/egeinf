f = open('27-13b__35x4q.txt')
n = int(f.readline())
a = [int(i) for i in f]
"""k14 = len(x for x in a if x % 14 == 0)
k7 = len(x for x in a if x % 7 == 0)
k2 = len(x for x in a if x % 2 == 0)
r = k14*k2 + k14*k7 + k14*(k14 - 1) // 2 + k14*n
"""



m2 = m7 = m14 = r = 0
m = mc = r = 10**10
for i in range(n-7):
    if a[i] % 2 == 0:
        m2 += 1
    if a[i] % 7 == 0:
        m7 += 1
    if a[i] % 14 == 0:
        m14 += 1

    if a[i+7] % 14 == 0:
        r += i+1
    elif a[i+7] % 7 == 0:
        r += m2
    elif a[i + 7] % 2 == 0:
        r += m7
    else:
        r += m14

print(r)

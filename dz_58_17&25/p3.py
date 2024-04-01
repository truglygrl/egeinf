f = open('17-381__335v8.txt')
a = [int(i) for i in f]
m39 = max(i for i in a if (len(str(abs(i))) == 4) and (abs(i) % 100 == 39))
print(m39)
c = 0
mx = -1000000000000000000
for i in range(len(a) - 1):
    if (int(len(str(abs(a[i]))) == 4) != int(len(str(abs(a[i+1]))) == 4)) and ((a[i] + a[i+1])**2 <= m39):
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)
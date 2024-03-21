r = 0

f = open('27-37b__33t98.txt')
n = int(f.readline())
a = [int(k) for k in f]
mn = [0]*10001
sm = [0]*20002
print(n)
for i in range(n-2):
    mn[a[i]] += 1
    for j in range(10001-a[i+1]):
        sm[a[i+1] + j] += mn[j]
    r += sm[a[i+2]]
print('wjff')
print(r)
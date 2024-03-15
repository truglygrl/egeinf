f = open('11_B__1vjye.txt')
#f = open('11_A__1vjyd.txt')#еобходимо найти в заданной серии показаний прибора максимальное произведение двух показаний, кратное 15, между моментами которых прошло не более 8 минут
n = int(f.readline())
k = 8
mx = -100000000000000000000
p = [0]*15
a = [int(j) for j in f]
for i in range(n-k):
    p[a[i] % 15] = max(p[a[i] % 15], a[i])
    for pa in p:
        if (pa*a[i+k]) % 15 == 0:
            mx = max(mx, pa*a[i+k])

print(mx)
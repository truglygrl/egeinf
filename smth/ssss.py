n = int(input())
m = int(input())
k = int(input())
t = int(input())

if m//k == m/k:
    print(n)

click = 0

if k > m and k-m > t:
    print(n)
elif k < m and m - k < t:
    while m-click*k>0:
        click += 1

    if -(m-(click + 1)*k)


elif k-m == t:
    print(n-t)

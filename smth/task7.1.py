arr = list(map(int,input().split(' ')))
ap =[]
n = len(arr)
if n % 2 == 0:
    for i in range(n//2):
        ap.append(arr[i])
        ap.append(arr[n - i - 1])
else:
    for i in range(n//2 + 1):
        if i == n // 2:
            ap.append(arr[n//2])
        else:
            ap.append(arr[i])
            ap.append(arr[n - i - 1])
print(*ap)
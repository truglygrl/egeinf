a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

ms = 0
m = [0] * 60
b = [0]*60
vse = [0]*60
r = 0

for i in range(n - 1):
    vse[a[i] % 60] += 1
    if a[i] > 80:
        b[a[i] % 60] += 1

    if a[i+1] > 80:
        r += vse[a[i+1] % 60]
    else:
        r += b[a[i+1] % 60]
print(r)
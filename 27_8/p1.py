#7&9 or 1&3
# k = 6
n = int(input())
r = 0
a = []
for i in range(n):
    a.append(int(input()))
c = [0]*10
for i in range(n-6):
    c[a[i] % 10] += 1
    if a[i+6] % 10 == 1:
        r += c[3]
    if a[i+6] % 10 == 3:
        r += c[1]
    if a[i+6] % 10 == 7:
        r += c[9]
    if a[i+6] % 10 == 9:
        r += c[7]
print(r)
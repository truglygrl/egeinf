a = [7392, 2345, 263, 8372, 372, 1836, 8326, 9736, 822, 6183]
n = 10
mx = 0
s = 0
for i in range(n):
    s += a[i]
    if s == 10000:
        print(i, a[i])
print(mx)
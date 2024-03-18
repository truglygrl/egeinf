f = open('27-75a__2zeg5.txt')
n = int(f.readline())
a = [int(i) for i in f]
mx = -1000000000000000
for i in range(len(a)):
    s = 0
    for j in range(i, len(a)):
        s += a[j]
        if s == 1806387:
            print('ssssssssssssssssssssss')
            print(j - i + 1)
print(mx)

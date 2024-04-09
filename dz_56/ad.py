f = open('266__1vi95.txt')
a = sorted(int(i) for i in f)
k10 = len(a)//10
b = a[::-1]
maxs = [int(i) for i in b[:k10]]
print(len(maxs), k10)
b = []
for i in range(len(a)):
    if i == 0:
        b.append(a[i])
    if (i+1) % 10 != 0:
        b.append(a[i])
    else:
        b.append(maxs[0])
        maxs.pop(0)
    if i < 20:
        print(b)
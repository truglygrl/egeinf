s = []
for x in range(1686, 13276):
    fl = 0
    for a in str(x):
        if int(a) % 2 == 0:
            fl = 1
            break
    if fl == 0:
        s.append(x)
t = [sum(int(i) for i in str(x)) for x in s]
print(sum(t))
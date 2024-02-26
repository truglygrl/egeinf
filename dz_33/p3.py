c = 0
for i in range(5, 1000):
    r = bin(i)[2:]
    if r.count('1') > r.count('0'):
        r = r + '0'
    if len(r) % 2 == 0:
        r = r[:len(r)//2 - 1] + r[len(r) // 2 + 1:]
    elif len(r) % 2 != 0:
        r = r[:len(r)//2 - 1] + r[len(r)//2 + 2:]

    if int(r, 2) == 58:
        c += 1
        print(i)
print(c)
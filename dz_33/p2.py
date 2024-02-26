for i in range(1, 1000):
    r = bin(i)[2:]
    if i % 2 == 0:
        r = r + bin(r.count('1'))[2:]
    else:
        r = '1' + r + '00'
    if int(r, 2) > 215:
        print(int(r, 2), i)
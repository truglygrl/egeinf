for n in range(1, 1999):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '1'
    else:
        r = r + '0'
    a = int(r, 2)
    if a % 2 == 0:
        r = r + '1'
    else:
        r = r + '0'
    if int(r, 2) < 109:
        print(int(r, 2))
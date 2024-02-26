for n in range(1, 300):

    r = bin(n)[2:]
    #print(r, '1')
    if r.count('0') == r.count('1'):
        r = r + r[-1]
    else:
        if r.count('0') < r.count('1'):
            r = r + '0'
        else:
            r = r + '1'
    #print(r, '2')
    if r.count('0') == r.count('1'):
        r = r + r[-1]
    else:
        if r.count('0') < r.count('1'):
            r = r + '0'
        else:
            r = r + '1'
    if (int(r, 2) % 3 == 0) and (int(r, 2) % 6 != 0):
        print(n)
for i in range(4, 1000):
    s = '5' + '7'*(i-2) + '5'
    while '577' in s or '775' in s:
        if '577' in s:
            s = s.replace('577', '755', 1)
        else:
            s = s.replace('775', '57', 1)
    if (sum([int(x) for x in s]) % 2 == 0) and (sum([int(x) for x in s]) > 223):
        print(i)
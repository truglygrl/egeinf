for i in range(100, 100000):
    s = '5'*i
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)

    if '5' not in s:
        print(i, s)
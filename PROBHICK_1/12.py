for i in range(100, 1000):
    a = '0' + i*'2' + '0'
    while '00' not in a:
        a = a.replace('01', '220', 1)
        a = a.replace('02', '1013', 1)
        a = a.replace('03', '120', 1)
    if (a.count('1') == 13) and (a.count('2') == 18):
        print(i)


"""b = '1'*13 + 18*'2'
while True:
    b = b.replace('220', '01', 1)
    b = b.replace('1013', '02', 1)
    b = b.replace('120', '03', 1)
    if len(b) > 31:
        print(len(b))"""
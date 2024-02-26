a = '0123456789a'
for x in a:
    s1 = '348' + x + '5'
    s2 = '1' + x + '111'
    r = int(s1, 11) + int(s2, 11)
    if r % 8 == 0:
        print(int(x, 11), r//8)
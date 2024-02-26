a = '0123456789abcdefghijklm'
for x in a:
    s1 = '14' + x + '4d'
    s2 = 'a' + x + 'f111'
    r = int(s1, 23) + int(s2, 23)
    if r % 17 == 0:
        print(r//17)

for i in range(101, 120):
    s = '6' * i
    while '666' in s:
        s = s.replace('666', '0', 1)
        s = s.replace('000', '66', 1)
    if s == '006':
        print(s, i)
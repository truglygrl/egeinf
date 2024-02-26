for i in range(123, 1000):
    s = '3'*i
    while '3333' in s:
        s = s.replace('3333', '555', 1)
        s = s.replace('5555', '33', 1)
    if s.count('3') == 5:
        print(i)
for x in range(1, 100):
    for y in range(1, 100):
        s = '3' + '4'*x + '8'*y + '3'
        while '38' in s or '34' in s:
            s = s.replace('38', '434', 1)
            s = s.replace('34', '188', 1)
        if s.count('4') == 39 and s.count('8') == 37:
            print(x+y)
for i in range(150, 300):
    s = '6'*i
    while '6666' in s or '9999' in s:
        if '6666' in s:
            s = s.replace('6666', '699', 1)
        else:
            s = s.replace('9999', '6', 1)
    a = s[151:501]
    if a.count('9') == a.count('6')*2:
        print(i)
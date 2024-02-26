s = '0'*400 + '1'
a = []
while '0000' in s or '111' in s:
    if '0000' in s:
        s = s.replace('0000', '110', 1)
    else:
        s = s.replace('111', '0', 1)
    if len(s) == 7:
        print(s)
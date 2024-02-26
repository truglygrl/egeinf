s = '1'*100 + '2'*200 + '3'
while '12' in s or '13' in s or '3333' in s:
    if '23' in s:
        s = s.replace('23', '3', 1)
    elif '13' in s:
        s = s.replace('13', '33', 1)
    elif '333' in s:
        s = s.replace('333', '3', 1)
print(s)
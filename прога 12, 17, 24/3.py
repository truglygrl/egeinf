s = '0' + '1'*70
while '01' in s or '211' in s or '3111' in s:
    if '01' in s:
        s = s.replace('01', '2', 1)
    elif '211' in s:
        s = s.replace('211', '3', 1)
    else:
        s = s.replace('3111', '0', 1)
print(s)
print(sum(int(i) for i in s))
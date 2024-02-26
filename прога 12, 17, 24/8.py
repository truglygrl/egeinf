s = '6'*1000
while '666' in s or '333' in s:
    if '333' in s:
        s = s.replace('333', '6', 1)
    else:
        s = s.replace('666', '3', 1)
print(s)
s = '6'*753
while '6666' in s or '5555' in s:
    if '5555' in s:
        s = s.replace('5555', '6', 1)
    else:
        s = s.replace('6666', '5', 1)
print(s)
s = '1' * 80
while '2121' in s or '111' in s:
    if '2121' in s:
        s = s.replace('2121', '2', 1)
    else:
        s = s.replace('111', '12', 1)
print(s)
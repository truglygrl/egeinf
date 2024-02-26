s = '7'*276
while '777' in s or '66' in s:
    if '66' in s:
        s = s.replace('66', '7', 1)
    else:
        s = s.replace('777', '6', 1)
print(s)
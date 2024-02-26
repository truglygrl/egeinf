s = '5'*1000
while '55555' in s:
    if '777777' in s:
        s = s.replace('777777', '5', 1)
    if '55555' in s:
        s = s.replace('55555', '7', 1)
print(s)
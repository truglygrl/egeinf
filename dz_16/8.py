s = '7'*125
while '777' in s:
    if '7777' in s:
        s = s.replace('7777', '6', 1)
    if '666' in s:
        s = s.replace('666', '7', 1)
print(s)
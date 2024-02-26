s = 13*'12'
while '12' in s or '2222' in s:
    s = s.replace('12', '2', 1)
    s = s.replace('222', '2', 1)
print(s)
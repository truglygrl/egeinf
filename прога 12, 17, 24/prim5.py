s = '563' * 121
while '56' in s or '3333' in s:
    s = s.replace('56', '3', 1)
    s = s.replace('3333', '3', 1)
print(s)
    
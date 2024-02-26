s = '9'*248 + '0'*448
c = 0
while ('99999' in s) or ('00000' in s):
    if '99999' in s:
        s = s.replace('99999', '099', 1)
    else:
        s = s.replace('00000', '009', 1)
    c += 1
print(c)
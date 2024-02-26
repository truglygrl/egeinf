s = '5'*1024
c = 0
while ('55555' in s ) or ('33333' in s):
    if '55555' in s:
        s = s.replace('55555', '333', 1)
    else:
        s = s.replace('33333', '555', 1)
    c += 1
print(s)
print(c)
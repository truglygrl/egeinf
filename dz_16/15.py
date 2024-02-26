x = 12**34 + 7*12**26 - 3*12**16 + 2*12**5 + 552
d = '0123456789ab'
s = ''
print(x)
print(hex(x))
c = 0
while x > 0:
    if x % 12 < 10:
        s = str(x%12) + s
        x = x // 12
        c += 1
    elif x % 12 == 10:
        s = 'a' + s
        x = x // 12
    elif x % 12 == 11:
        s = 'b' + s
        x = x // 12

print(s)
print(c)
print(len(s))
print(len(set(s)))
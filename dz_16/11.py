x = (16**23)*(4**11) - 4**7 + 132
print(x)
s = ''
while x > 0:
    s = str(x%4) + s
    x = x//4
print(s)
print(s.count('3'))
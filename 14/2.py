def f(x, c):
    a = ''
    while x > 0:
         a = str(x%c) + a
         x = x // c
    return int(a)

#s = '0123456789abcde'
a1 = '0123456789abcde'
for i in a1:
    s1 = '123' + i +'5'
    s2 = '1' + i + '233'
    s = int(s1, 15) + int(s2, 15)
    if s%14==0:
        print(i, s // 14)

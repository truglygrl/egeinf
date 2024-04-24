d = set()
#+1 '0'
#+3 '0'
#*2 '1'
#*3 '1'
def f(a, c, m1):
    if c > 12:
        return 0
    if c == 12:
        d.add(a)
        return
    if c < 12:
        if m1 == '0':
            f(a * 2, c + 1, '1')
            f(a * 3, c + 1, '1')
        elif m1 == '1':
            f(a + 1, c + 1, '0')
            f(a + 3, c + 1, '0')
        else:
            f(a + 1, c + 1, '0')
            f(a + 3, c + 1, '0')
            f(a * 2, c + 1, '1')
            f(a * 3, c + 1, '1')

f(6, 0, '')
print((len(d)))
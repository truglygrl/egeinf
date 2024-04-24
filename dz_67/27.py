d = set()
def f(a, c, m1, m2):
    if c > 11:
        return 0
    if c == 11:
        d.add(a)
        return

    if m1 == m2 == '1':
        f(a * 2, c + 1, m2, '2')
    elif m1 == m2 == '2':
        f(a + 2, c + 1, m2, '1')
    else:
        f(a*2, c + 1, m2, '2')
        f(a+2, c + 1, m2, '1')



f(1, 0, '', '')
print((len(d)))
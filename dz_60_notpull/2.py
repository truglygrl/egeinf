def f(a, m1, m2):
    if a >= 68:
        return 0
    t = []    #t = [f(a+3), f(a+6), f(a*3)]#1, 2, 3
    if m2 != 1:
        t += [f(a+3, 1, m1)]
    if m2 != 2:
        t += [f(a+6, 2, m1)]
    if m2 != 3:
        t += [f(a*3, 3, m1)]
    h = [x for x in t if x <= 0]
    if h:
        return -max(h) + 1
    return -max(t)

for i in range(1, 68):
    if f(i, 0, 0) == 3:
        print(i)
from fnmatch import *
def f(a):
    s = set()
    for w in range(2, int(a**0.5) + 1):
        if a % w == 0:
            s.add(w)
            s.add(a // w)
    return s
for i in range(177, 10**5+1):
    if fnmatch(str(i), '1*77'):
        t = sorted(f(i))
        fl = 0
        for d in range(len(t)-1):
            for q in range(d+1, len(t)-1):
                if ((t[q]*t[d]) == i) and (t[q] != t[d]) and (len(f(d)) == 0) and (len(f(q)) == 0):
                    fl = 1
                    break
        if fl == 1:
            print(i)
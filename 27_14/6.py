def f(st, end, x):
    if st <= x <= end:
        return True
    return False
lens = []
for a in range(1, 500-1):
    fl = 0
    for b in range(a+1, 500):
        for i in range(1, 1000):
            if ((f(a, b, i) <= (f(12, 20, i)) or (f(25, 58, i)))) == False:
                fl = 1
                break
        if fl == 0:
            lens.append(b-a)
print(max(lens))
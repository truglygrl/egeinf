from fnmatch import *
for x in range(1, 10**8+1):
    s = str(x)
    c = set()
    if s[-1] != '7':
        if fnmatch(s, '*562??90') and (not (fnmatch(s, '?3*7'))):
            if x % 394 == 0:
                print(x, x // 394)

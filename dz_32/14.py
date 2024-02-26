from fnmatch import *
for x in range(1, 10**5+1):
    s = str(x)
    c = set()
    if fnmatch(s, '*9*270*'):
         if x % 34 == 0:
            print(x, x // 34)

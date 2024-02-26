from fnmatch import *
for x in range(1, 10**6+1):
    s = str(x)
    c = set()
    if fnmatch(s, '3*4?7?9'):
         if x % 37 == 0:
            print(x, x // 37)

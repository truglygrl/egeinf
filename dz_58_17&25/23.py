from fnmatch import *

c = 0
for x in range(9001230, 9001230*10):
    s = str(x)
    if (((int(s[-1])*4) + int(s[-2])) % 13 == 0) and fnmatch(s, '90?123?'):
        print(x)
        c += 1
print(c)
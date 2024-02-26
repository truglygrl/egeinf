from fnmatch import *
for x in range(126, 10**6, 126):
    if (x % 126 == 0) and (x % 19 != 0):
        if fnmatch(str(x), '?4*2?6'):
            print(x)

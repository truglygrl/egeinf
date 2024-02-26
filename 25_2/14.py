from fnmatch import *
for x in range(2409, 10**6, 2409):
    if fnmatch(str(x), '7*9??*1'):
        print(x)

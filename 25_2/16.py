from fnmatch import *
for i in range(61, 10**6, 61):
    if fnmatch(str(i), '31*2?9*'):
        print(i)
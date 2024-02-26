from fnmatch import *
for x in range(2048, 10**7, 2048):
    if fnmatch(str(x), '*6*?3*96'):
        print(x, x // 2048)
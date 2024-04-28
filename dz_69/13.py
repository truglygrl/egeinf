from fnmatch import *
for x in range(908548, 10**10+1, 1724):
    if x % 1724 == 0:
        if fnmatch(str(x), '9?99*16'):
            print(x, x // 1724)
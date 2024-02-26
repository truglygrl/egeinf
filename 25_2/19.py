from fnmatch import *
for i in range(29, 10**8, 29):
    if fnmatch(str(i), '34?8?97'):
        print(i, i // 29)

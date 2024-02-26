from fnmatch import *
for i in range(12345, 10**10, 12345):
    if fnmatch(str(i), '21?498*4*'):
        print(i, i // 123456)
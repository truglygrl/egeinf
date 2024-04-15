from fnmatch import *
for x in range(123450705, 10**9, 21):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x // 21)
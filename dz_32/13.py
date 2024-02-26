from fnmatch import *
for x in range(1, 10**7+1):
    s = str(x)
    c = set()
    if s[0] == '8':
        if fnmatch(s, '8?0*191'):
            if (x % 19 == 0) and (x % 2 != 0):
                print(x)

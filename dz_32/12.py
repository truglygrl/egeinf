from fnmatch import *
for x in range(1, 10**7+1):
    s = str(x)
    c = set()
    if s[0] == '1':
        if fnmatch(s, '1*2?3*5'):
            if (x % 123 == 0) and (x % 17 == 0):
                print(x)

from fnmatch import *
for x in range(1000746, 10**10+1, 3147):
    s = str(x)
    if (s[0] == '1') and (s[-1] == '1') and (s[-3] == '2'):
        if fnmatch(s, '1*4302?1'):
            print(x)

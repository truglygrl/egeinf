from fnmatch import *
for x in range(95, 10**6, 95):
    if fnmatch(str(x), '5??1*?0'):
        if (str(x).count('5') == 1) and (str(x).count('1') == 1) and (str(x).count('0') == 1):
            print(x)

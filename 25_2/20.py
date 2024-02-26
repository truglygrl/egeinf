from fnmatch import *
for i in range(111, 10**7, 111):
    if fnmatch(str(i), '9??5*1*?3'):
        print(i)
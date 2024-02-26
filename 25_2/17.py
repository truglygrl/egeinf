from fnmatch import *
for x in range(387, 10**7, 387):
    if fnmatch(str(x), '*16*9?0?'):
        print(x)
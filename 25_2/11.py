from fnmatch import*
for x in range(61, 10**6, 61):
    if (x % 2 != 0) and (x % 19 != 0):
        if fnmatch(str(x), '5*9?*2?'):
            print(x)

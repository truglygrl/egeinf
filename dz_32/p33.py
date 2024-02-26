from fnmatch import *
for x in range(1000000, 10**10+1):
    s = str(x)
    c = set()
    if fnmatch(s, '1?2*0*2?1'):
        if x ** 0.5 == int(x ** 0.5):
            print(x, x**0.5)
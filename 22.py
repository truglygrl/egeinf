from fnmatch import *

c = set()

for n in range(0, 10**7, 17):
    s = str(n)

    if fnmatch(s, '123*4?6'):
        print(n, n//17)
        c.add(s)
        c.add(n//17)

#print(c)
#print(len(c))
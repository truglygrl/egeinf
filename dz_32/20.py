k = 0
from fnmatch import *
for x in range(1, 10**6+1):
    d = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d += i + x // i
    d = str(d)
    if fnmatch(d, '2*45'):
        k += 1
print(k)
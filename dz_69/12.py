from fnmatch import *

for n in range(26895, 10**10+1, 8965):
    if n % 8965 == 0:
        if fnmatch(str(n), '?3*313?'):
            print(n, n // 8965)
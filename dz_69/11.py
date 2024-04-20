from fnmatch import *

for n in range(3500690, 10**9, 1777):
    if fnmatch(str(n), '35??78*9'):
        print(n, n // 1777)
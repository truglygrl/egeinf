from fnmatch import *
def f(a):
    for l in range(2, a):
        if a % l == 0:
            return False
    return True


for x in range(90713, 10**7+1):
    if fnmatch(str(x), '9?7*13'):
        if f(x):
            print(x)
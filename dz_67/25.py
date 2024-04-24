d = set()
def f(a, c):
    if c > 11:
        return 0
    if c == 11:
        d.add(a)
        return
    if c < 11:
        f(a-1, c+1)
        f(a - 5, c + 1)
        f(a*2, c + 1)
f(2, 0)
print(len(d))
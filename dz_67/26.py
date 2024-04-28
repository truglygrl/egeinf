d = set()
def f(a, c):
    if c > 7:
        return 0
    if c == 7:
        d.add(a)
        return
    if c < 7:
        f(a-2, c+1)
        f(a-3, c + 1)
        f(a // 2, c + 1)
f(220, 0)
print(len(d))
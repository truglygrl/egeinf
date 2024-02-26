n = int(input())
mc = mn = ms = 0
x = int(input())
for i in range(n - 1):
    if x > mc and x % 2 == 0:
        mc = x
    if x > mn and x % 2 != 0:
        mn = x
    x = int(input())
    if (x + mc > ms) and ((x + mc) != 0) and (mc > 0):
        ms = x + mc
    if (x + mn > ms) and ((x + mn) != 0) and (mn > 0):
        ms = x + mn
print(ms)
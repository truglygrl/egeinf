def f(a):
    if a >= 25:
        return 0
    t = [f(a+2), f(a*2)]#2 el for a
    n = [i for i in t if i <= 0]#negative
    if n:
        return -max(n) + 1#win
    else:
        return -max(t)#lose
for i in range(1, 30):
    print(i, f(i))

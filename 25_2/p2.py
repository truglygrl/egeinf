def f(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
k = 0
for x in range(105673, 220785):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            if f(i):
                c.add(i)
            if f(x//i):
                c.add(x // i)
    t = list(c)
    flag = 0
    if len(t) >= 3:
        for i in t:
            for j in t:
                for k in t:
                    if (i*j*k == x) and (i != k) and (i != j) and (j != k):
                        flag = 1

    if flag == 1:
        k += 1
print(k)
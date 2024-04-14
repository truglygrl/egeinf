def pr(n):
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True
def f(a):
    s = set()
    for d in range(2, int(a**0.5)+1):
        if a % d == 0:
            s.add(d)
            s.add(a // d)
    return s

ans = []
for x in range(351627, 428764):
    t = list(f(x))
    if len(t) > 1:
        for i in range(len(t) - 1):
            for j in range(i + 1, len(t)):
                if (t[i] * t[j] == x) and (t[i] != t[j]) and (pr(t[i])) and (pr(t[j])):
                    ans.append(x)


print(len(ans), sum(ans) / len(ans))

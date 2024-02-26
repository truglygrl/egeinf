def p(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    arr = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            arr.append(i)
            if i != x // i:
                arr.append(x//i)
        if len(arr) > 6:
            return []

    s = []
    for j in arr:
        if p(j):
            s.append(j)
    if len(s) == 3:
        s = sorted(s)
        if (int(s[0])*int(s[1])*int(s[2])) == x:
            if ((int(s[0]) % 10 == int(s[1]) % 10) and (int(s[1]) % 10 == int(s[2]) % 10)):
                return True
    return False

ans = []
for n in range(416782, 498325):
    if f(n):
        ans.append(n)
print(len(ans), (max(ans) - min(ans)))
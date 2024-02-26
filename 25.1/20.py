def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
print(f(89472))
cnt = 0

for n in range(156367, 178946):
    c = set()
    for i in range(2, int(n**0.5)+1):
        if f(i) and(f(n // i)) and ((n//i)*i == n):
            c.add(i)
            c.add(n//i)
            if len(c)==2:
                cnt += 1
                break
print(cnt)
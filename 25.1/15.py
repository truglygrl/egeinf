def f(x):
    for i in range(2, int(x**0.5)+1):
        if n % i == 0:
            return False
    return True

cnt = 1
for n in range(9080350, 9080446):
    if f(n):
        print(cnt, n)
        cnt += 1
def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
cnt = 1
for n in range(4301614, 4301718):

    c = set()
    if f(n):
        print(cnt, n)
    cnt += 1
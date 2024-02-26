for n in range(157898, 157991):
    c = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            c.add(i)
            c.add(n//i)
    if len(c) == 6:
        print(*sorted(c))





def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for x in range(4301614, 4301718):
    if f(x):
        print(x)
"""
print(f(345329))

x = 309829
for i in range(2, int(x**0.5)+1):
    if x % i == 0:
        if f(i):
            print(i)
"""
print(13338%10)
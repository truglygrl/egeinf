x = int(input())
L = 0; M = 0
while x > 0:
    L = L + (x % 10)
    if x % 2 == 0:
        M = M + 1
    x = x // 10
print(L, M)
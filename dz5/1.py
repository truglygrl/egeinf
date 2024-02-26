n = int(input())
a = []
for i in range(n):
    b = int(input())
    if b % 7 == 0 and b % 9 != 0:
        a.append(b)
print(max(a))
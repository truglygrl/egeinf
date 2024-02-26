n = int(input())
a = []
for i in range(n):
    b = int(input())
    if len(str(b)) == 2 and b % 8 == 3:
        a.append(b)
print(min(a))
a, b = map(int, input().split())
a = str(a)
b = str(b)

bulls = 0
cows = 0

for i in range((len(a))):
    if b[i] == a[i]:
        bulls += 1
    elif b[i] in a:
        cows += 1
print("быки", bulls)
print("коровы", cows)
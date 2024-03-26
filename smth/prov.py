cnt = 0
summ = 0
s1 = ''
for i in range(100, 1000):
    s = str(i)
    for j in range(len(s)):
        s1 = s1 + s[-j-1]
    if s1 == s:
        summ+=i
print(summ)
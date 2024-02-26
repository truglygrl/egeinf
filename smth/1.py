s = input()
summ = int(s[0])
for i in range(2, len(s)):
    if s[i-1] == '-':
        summ -= int(s[i])
    elif s[i-1] == '+':
        summ += int(s[i])
print(summ)
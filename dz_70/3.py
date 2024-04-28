s = open('Задание_24__t2na.txt').readline()
l = 0
for i in range(1, len(s)-2):
    if s[i] == s[i+2] == 'V':
        l += 1

print(l)
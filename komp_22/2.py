f = open('24_5171.txt')
s = f.readline()
c = cm = 0
for i in range(0, len(s)-1, 2):
    if 'CA' in s[i:i+2]:
        c += 2
        cm = max(cm, c)
    else:
        c = 0

print(cm)
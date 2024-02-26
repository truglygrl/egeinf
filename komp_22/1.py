c = cm = 1
f = open('24_2423.txt')
s = f.readline()
#s = 'XXYssesswsqsYYZZZ'
for i in range(len(s)-1):
    if s[i] < s[i+1]:
        c += 1
        cm = max(cm, c)
    else:
        c = 1
    #print(s[i:i + 3], c)
print(cm)

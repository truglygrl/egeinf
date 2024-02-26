f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/4__1tixx.txt')
s = f.readline()
l = lm = 0
for i in range(len(s)-2):
    if s[i] != s[i+1] != s[i+2]:
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0
print(lm+2)
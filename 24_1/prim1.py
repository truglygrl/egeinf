f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/24-211.txt')
s = f.readline()
l = lm = 0
for i in range(0, len(s), 3):
    if s[i:i+4] in ['ABEC', 'BDAC', 'CAFB', 'CFBA']:
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0
print(lm)
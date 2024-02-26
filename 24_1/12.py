f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/12.txt')
s = f.readline()
#s = 'sdfLRDLRDLRDDRLDRLjkdfkdjflkLRDDRLLRDLRD'
l = lm = 0
for i in range(2, len(s), 3):
    if (s[i:i+3] in ['LRD','DRL']):
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0
print(lm*3)
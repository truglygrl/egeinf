f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.2/24__1zitu.txt')
s = f.readline()
a = []
s0 = 'ABCDE'
#s = 'AABBCCCDDEEEEE'
for k in s0:
    l = lm = 0
    #if k in s:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] == k:
            l += 1
            if l > lm:
                lm = l
        else:
            l = 0

    a.append(lm+1)
print(a)
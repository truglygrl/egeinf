f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/11.txt')
s = f.readline()
#s = 'AGsTNs'
""""
c = cm = 0
print(len(s))
for i in range(len(s)):
    for k in range(len(s)):
        flag = 0
        if ('AG' in s[i:k]) and ('TN' in s[i:k]):
            flag = 1
            break
        if flag == 0:
            c = k-i
            if c > cm:
                cm = c

print(cm+1)"""







a = max(map(len,s.replace('AG', 'A G').split())) #без пары AG
b = max(map(len,s.replace('TN', 'T N').split())) #без пары
print(max(a, b))
""""
s = s.split()
print(s)
t = list(map(len, s))
print(s)
print(max(t))
k = 0"""

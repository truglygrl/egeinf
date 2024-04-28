f = open('Задание_24__k3bz__t57g.txt')
s = f.readline()
maxim = 0
counter = 0
flag = False
for i in range(1, len(s)-1):
    if s[i] < s[i-1] and s[i] < s[i+1]:
        counter = 0
        flag = True
    if flag:
        counter += 1
        if counter > maxim:
            maxim = counter
print(maxim)
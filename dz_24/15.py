f = open('24_3__1kacn.txt')
s = f.readline()
#s = '123214444444123211232123211'
c = 0

for i in range(len(s)-4):
    t = s[i:i+5]
    if (t[0] == t[-1]) and (t[1] == t[-2]):
        c += 1
print(c)

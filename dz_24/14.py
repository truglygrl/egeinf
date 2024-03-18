f = open('24_2__1kacj.txt')
a = '02468'
s = f.readline()
#s = '12341234123416161616sssssssss5656787854'
b = '13579'
k = km = 0
print(s)
for i in range(0, len(s)-3, 4):
    if s[i] in b and s[i+1] in a and s[i+2] in b and s[i+3] in a:
        k += 4
        km = max(k, km)
    else:
        k = 0
print(km)

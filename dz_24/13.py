k = km = 0
f = open('24__1jdz4.txt')
s = f.readline()
##s = 'XYXXYYZZYZYXXYZ'
s = s.replace('X', '*').replace('Y', '!').replace('Z', '*')
#print(s)
for i in range(3, len(s)-4, 4):
    if s[i:i+4] == '!**!':
        #print(s[i:i+4])
        k += 1
        km = max(km, k)
    else:
        k = 0
print(km*4)
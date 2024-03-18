f = open('6__1dn86.txt')
s = [i for i in f.readline()]
#s = 'aslkjd11111jklsdkfj999999999'
print(s[0], s[-1])
k = km = 1
c = ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        k += 1
        if k > km:
            km = k
            c = s[i]
    else:
        k = 1
print(km, c)

s = list(reversed(s))
for i in range(len(s)-6):
    t = s[i:i+6]
    if len(set(t)) == 1:
        print(t)
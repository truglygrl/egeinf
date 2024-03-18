f = open('8__19jzo.txt')
s = f.readline()
#s = 'aaaa11111oedm333333aaaaaaoooooo'
k = km = 0
c = ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        k += 1
        if k > km:
            km = k
    else:
        k = 0
km = km+1
for i in s:
    if i*km in s:
        c += i

c = ''.join(sorted(set([i for i in c])))
print(km,c)
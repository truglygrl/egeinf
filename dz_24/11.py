f = open('7__1dn85.txt')
s = f.readline()
#s = '123451234ddddd512345'
k = km = 4
for i in range(len(s)-4):
    t = s[i:i+5]
    #print(t, set(t))
    if len(set(t)) == 5:
        k += 1
        km = max(k, km)
    else:
        k = 4
print(km)
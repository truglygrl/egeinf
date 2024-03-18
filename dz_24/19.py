f = open('24__1nxrx.txt')
s = f.readline()
#s = 'BDEACCACddddddCACC'
k = km = 0
for i in range(2, len(s)-2, 3):
    if s[i:i+3] == 'BDE' or s[i:i+3] == 'ACC':
        k += 1
        km = max(k, km)
    else:
        k = 0
print(km)
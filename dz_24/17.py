f = open('7__1ncxh.txt')
s = f.readline()
#s = 'FDEFDEvvvvvvvvvvvvFDEF'
s = s.replace('FDE', '***')
k = km = 0
for i in range(0, len(s)-1, 3):
    if s[i:i+3] == '***':
        k += 1
        km = max(k, km)
    else:
        k = 0
print(km)
print(s.find('***'))
print(s[165:175])
f = open('24_1143.txt')
s = f.readline()
#s = 'AkkkkkkkkFAFAAFAkkkkkkkkkkkkkFAkkkkkkkF'
c = 0
s = s.replace('FA', 'F A')
s = s.split(' ')
print(s)
t = [len(x) for x in s]
#print(t)
c = [int(i) for i in t if (i >= 7) and (i <= 10)]
print(len(c))
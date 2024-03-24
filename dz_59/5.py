s = open('24-5__33ojv.txt').readline()
for i in s:
    if i in 'YO':
        s = s.replace(i, 'g')
    if i in 'ZXP':
        s = s.replace(i, 's')


s = s.replace('gs', '*')
t = [len(x) for x in s.split('*')]
mx = -10
for i in range(len(t)):
    mx = max(mx, sum(t[i:i+5]))
    #print(t[i:i+6])
print(mx)
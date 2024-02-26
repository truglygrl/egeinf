f = open('24_1.txt')
s = f.readline()
s = s.replace('A', '*')
s = s.replace('B', '*')
s = s.split('*')
t = [len(i) for i in s]
mx = -100
for i in range(len(t)-2):
    mx = max(mx, sum(t[i:i+3]))
print(mx+2)
from fnmatch import *
s = open('24__1udcl.txt').readline()
s = s.replace('TT', 'T T').split()
mx = -100000
for q in s:
    for i in range(len(q)-9):
        if (q[i+0] == '1') and (q[i+1] == '2') and (q[i+4] == '3') and (q[i+5] == '4') and (q[i+9] == '5'):
            print(int(q[i:i+10]))
            mx = max(mx, int(q[i:i+10]))
print(mx)
print(sum(int(x) for x in '1299349995'))
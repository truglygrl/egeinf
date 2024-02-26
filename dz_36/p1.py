f = open('24-224__2pt9p.txt')
s = f.readline()
s = s.replace('BACAB', 'BAC_CAB').replace('CABAC', 'CAB_BAC')
print(s)
s = s.replace('BAC', '*').replace('CAB', '*')
print(s)
for i in range(len(s)):
    if '*'*i in s:
        print(i*3)
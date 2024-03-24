s = open('24_2__28yls.txt').readline()
s = s.replace('C', 'B')
s = s.replace('ABB', '*')
for i in range(len(s)):
    if i*'*' in s:
        print(i*3)

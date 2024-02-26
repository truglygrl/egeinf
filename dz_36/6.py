s = open('6__2pp78.txt').readline()
s = s.replace('YZX', '*').replace('ZXY', '*')
for i in range(len(s)):
    if '*'*i in s:
        print(i*3)
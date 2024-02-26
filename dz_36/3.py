s = open('3__2pp6v.txt').readline()
s = s.replace('DFAAB', '*')
s = s.split('*')
for i in range(5):
    print(s[i])
    print(s[i][-1])
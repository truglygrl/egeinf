s = open('7__2pp79.txt').readline()
#s = 'aaaaaaaaDFaaaaaaaaaaaaaLEaaaaaDFaaaaaLEaaaaaaaaaaa'
# 3957 получилось с D F
s = s.replace('LE', 'L E')
t = [len(i) for i in s.split()]
print(max(t))

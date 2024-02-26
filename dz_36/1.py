s = open('1__2pp6t.txt').readline()
s = s.replace('BD', 'B D')
s = s.split()
print(s)
t = [len(i) for i in s]
print(max(t))
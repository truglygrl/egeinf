s = open('8__2pp7a.txt').readline()
t = [len(i) for i in s.split('A')]
print(max(t))
s = open('24-2__33ojc.txt').readline()
t = [len(x) for x in s.replace('DA', 'D A').split('D A')]
print((max(t))+2)
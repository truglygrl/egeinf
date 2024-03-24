s = open('4__2pp6x.txt').readline()
#s = 'ooooooooooooooooooCEDAooooooooooooooooooooooCEDA'
s = s.split('CEDA')
t = [len(x) for x in s]
print(max(t) + 6)
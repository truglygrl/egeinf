f = open('1__19jvr.txt')#3830
s = f.readline()
#s = 'sssAAEBDssAAEBDsAAEBD'
k = 0
print(s.find('AAEBD'))
s = s.replace('AAEBD', '*****', 2)
print(s)
print(s.find('AAEBD'))
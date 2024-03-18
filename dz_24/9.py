f = open('1__1dn8n.txt')
s = f.readline()
#print(s.find('CCADE'))
#s = 'ССADEССADEССADEССADEaССADE'
s = s.replace('CCADE', '*****', 4)
#print(s)
print(s.find('CCADE')+1)
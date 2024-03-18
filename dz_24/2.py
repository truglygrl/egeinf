f = open('2.txt')
s = f.readline()
#s = 'ssssDBCDBCddddBDBDBBDBDBBDBDBBDBDBDB'
s = s.replace('C', '*').replace('D', '*').replace('B', '*')
print(s)
for i in range(len(s)):
    if '*'*i in s:
        print(i)
s = open('2__2pp6u.txt').readline()
s = s.replace('AAE', '*').replace('DBC', '*')
t = [len(x) for x in s if x == '*']
for i in range(len(s)):
    if '*'*i in s:
        print(i)
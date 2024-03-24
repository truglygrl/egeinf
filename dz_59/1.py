s = open('24-1__33oiz.txt').readline()
s = s.replace('CGG', '*').replace('DDG', '*')
for i in range(len(s)):
    if '*'*i in s:
        print(i)
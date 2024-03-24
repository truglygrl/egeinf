s = open('24_5__28ylm.txt').readline()
s = s.replace('C', 'A').replace('D', 'A')
for i in range(len(s)):
    if i*'A' in s:
        print(i)
s = open('5__2pp6z.txt').readline()
for i in range(len(s)):
    if 'L'*i in s:
        print(i)
s = open('Задание_24__tlln.txt').readline().replace('OSR', '*').replace('RSO', '*')

for i in range(len(s)):
    if i*'*' in s:
        print(i*3)
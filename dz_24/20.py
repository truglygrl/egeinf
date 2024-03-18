f = open('3__1tixu.txt')
s = f.readline()
k = km = 0
#s = 'EABEABEABEABEABEAB'
for i in range(2, len(s)-5, 3):
    if s[i:i+6] == 'EABEAB':
        if s[i+6] == 'E':
            print(s[i:i+9])

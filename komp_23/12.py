f = open('24_2503.txt')
s = f.readlines()
c = 0
for ss in s:
    c1 = c2 = 0
    for i in range(len(ss)-3):
        if (ss[i] == 'A') and (ss[i+1] == 'O') and (ss[i+2] == 'A'):
            c1 += 1
        if (ss[i] == 'O') and (ss[i+1] == 'A') and (ss[i+2] == 'O'):
            c2 += 1
    if c1 > c2:
        c += 1
print(c)
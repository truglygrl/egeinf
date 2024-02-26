f = open('24_2502.txt')
s = f.readlines()
c = 0
for ss in s:
    fl = 0
    for i in range(len(ss)-3):
        if (ss[i] == 'K') and (ss[i+2] == 'G') and (ss[i+3] == 'E'):
            fl = 1
            break
    if fl == 1:
        c += 1
print(c)
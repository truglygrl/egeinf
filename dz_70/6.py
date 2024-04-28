s = open('24__13oe8.txt').readline()
g = 'AOUEI'
lg = lgm = lc = lcm = 1
for i in range(len(s)-1):
    if (s[i] in g) and (s[i+1] in g):
        lg += 1
        lgm = max(lgm, lg)
    else:
        lg = 1
    if (s[i] not in g) and (s[i+1] not in g):
        lc += 1
        lcm = max(lc, lcm)
    else:
        lc = 1

print(lgm, lcm)
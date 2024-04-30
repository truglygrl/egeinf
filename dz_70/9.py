f = open('words__swpu.txt')
s = [x[:-1] for x in f]

p = 0
l = lm = m = 1
for d in s:
    c = [0] * 1000
    for i in range(len(d)-1):
        if ord(d[i]) == ord(d[i+1]) - 1:
            l += 1
            lm = max(l, lm)
            c[ord(d[i])] += 1
        else:
            l = 1
    m = max(m, lm)
    if lm == 5:
        print(chr(c.index(max(c))))
print(m)
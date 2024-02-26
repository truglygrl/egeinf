f = open('19.txt')
k = 0
for i in range(1):
    #t = sorted(int(x) for x in f.readline().split())
    t = [2, 6, 6, 6, 6]
    if len(set(t)) == 2:
        ff = ((t[0] == t[1]) and (t[1] == t[2])) + ((t[1] == t[2]) and (t[2] == t[3])) + ((t[2] == t[3]) and (t[3] == t[4]))
        if int(ff) >= 2:
            k += 1
            print(t)
print(k)
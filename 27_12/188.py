f = open('16.txt')

k = 0
for i in range(3000):
    t = sorted(int(x) for x in f.readline().split())
    if ((t[0] == t[1]) and (t[1] == t[2])) or ((t[1] == t[2]) and (t[2] == t[3])):
        k += 1
print(k)
f = open('26_5__3cjxc.txt')
n = int(f.readline())#pep
k = int(f.readline())#copms
a = []
t = [-1]*k
to = 60*5
tz = 60*23
for i in range(n):
    n1, n2 = map(int, f.readline().split())
    n1, n2 = n1, n1+n2
    if (n1 >= to) and (n2 <= tz):
        a.append([n1, n2])
a.sort()
k7 = w = 0
for n1, n2 in a:
    for i in range(k):
        if t[i] < n1:
            t[i] = n2 + 11
            w += 1
            if i == 6:
                k7 += 1
            break
print(w, k7)
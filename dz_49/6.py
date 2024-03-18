f = open('26_12__30v1f.txt')
n = int(f.readline())
k = int(f.readline())
clients = sorted(list(map(int, i.split())) for i in f)
table = [0]*k
ans1 = 0
ans2 = 0
print(k, n)
for client in clients:
    ok = False
    for i in range(k):
        if client[0] >= table[i]:
            ok = True
            table[i] = client[1] + 22
            ans1 += 1
            ans2 = i + 1
            print(table)
            break

    if not ok:
        mt = min(table)
        if client[0] + 3 >= mt:
            ind = table.index(mt)
            T = client[1] - client[0]
            if table[ind] + T <= 1200:
                table[ind] += T + 22
                ans1 += 1
                ans2 = ind + 1

print(ans1, ans2)
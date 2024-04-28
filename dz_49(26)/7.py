ans1 = ans2 = 0
f = open('26_10__30v17.txt')
b = int(f.readline())
k = int(f.readline())
table = [0]*k
clients = sorted(list(map(int, i.split())) for i in f)
for client in clients:
    ok = False
    print('client', client)
    for i in range(k):
        if client[0] >= table[i]:
            table[i] = client[1] + 15 + 2
            ok = True
            ans1 += 1
            ans2 = i + 1
            break
    if not ok:
        mt = min(table)
        if client[0] + 30 + 1 >= mt:
            ind = table.index(mt)
            T = client[1] - client[0]
            if table[ind] + T+1 <= 1260:
                table[ind] += T + 15+2
                ans1 += 1
                ans2 = ind + 1
print(ans1, ans2)
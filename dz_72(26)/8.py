f = open('26_2__3cjv5.txt')
n = int(f.readline()) #количество покупателей
k = int(f.readline()) #количество камер хранения в магазине
a = sorted((list(map(int, i.split()))) for i in f)
t = [-1]*k
win = last = 0
for pep in a:
    l = []
    for j in range(k):
        if t[j] < pep[0]:
            t[j] = pep[1]
            win += 1
            last = j + 1
            break
print(win, last)
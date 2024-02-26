f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/17-379.txt')

a = [int(i) for i in f]
m15 = max(i for i in a if i % 100 == 15)
c = ms = 0
for i in range(len(a)-2):
    if sum(a[i:i+3]) >= m15:
        t = [x for x in a[i:i+3] if x in range(1000, 10000)]
        print(t)
        if len(t) == 1:
            c += 1
            ms = max(ms, sum(a[i:i+3]))
print(c, ms)

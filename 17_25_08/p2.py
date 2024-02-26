f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/17_25_08/17-1.txt')
a = [int(i) for i in f]
sr = sum(a) / len(a)
c = 0
mx = -1000000000000000000
for i in range(len(a)-2):
    t1 = len([x for x in a[i:i+3] if x < sr])
    t2 = len([x for x in a[i:i+3] if abs(x) % 10 == 8])
    if (t1 >= 2) and (t2 >= 2):
        c += 1
        mx = max(sum(a[i:i+3]), mx)
print(c, mx)
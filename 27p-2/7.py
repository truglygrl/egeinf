f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27p-2/7.txt')
n = int(f.readline())
p = int(f.readline())
a = [int(i) for i in f]
print(n)
print(p)
print(a[58167])
sp = []
sv = []
l = 36846
for i in range(len(a)):
    if p <= i < l:
        sp.append(i)
    else:
        sv.append(i)
print(len(sp))
print(len(sv))

print(sum(sp))
print(sum(sv))
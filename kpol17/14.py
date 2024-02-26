f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2309.txt')
a = [int(i) for i in f]
mn4 =  min(x for x in a if x % 10 == 4)
mx4 =  max(x for x in a if x % 10 == 4)
s = mn4 + mx4
c = 0
mx = -1000000000000
for i in range(len(a)-1):
    if (a[i] + a[i+1]) < s:
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)
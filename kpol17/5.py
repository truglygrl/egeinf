f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_1993.txt')
a = [int(i) for i in f]
c = 0
mx = -100000000000000000000000000
for i in range(len(a) - 1):
    b = a[i]
    d = a[i+1]
    s = b+d
    if (s % 3 == 0) and (s % 6 != 0) and (abs(b*d) % 10 == 8):
        c += 1
        mx = max(mx, b+d)
print(c, mx)
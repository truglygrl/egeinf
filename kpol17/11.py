f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2002.txt')
a = [int(i) for i in f]
ans = []
for i in range(len(a)-3):
    if a[i] > a[i+1] > a[i+2] > a[i+3]:
        if (a[i] - a[i+3]) > 1000:
            ans.append(min(a[i], a[i+1], a[i+2], a[i+3]))
print(len(ans), sum(ans))
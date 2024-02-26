f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27p-2/10.txt')
n = int(f.readline())
k = int(f.readline())
a = [int(i) for i in f]
t1 = a[:k-1]# в т1 закидываю все элементы с 0 по к
t2 = a[k-1:] #в т2 закидваю все элементы с к по 0
t = t2 + t1#здесь получаю список т который начинается с a[k] и заканчивается a[k-1]
print(len(t), t[0], len(a), a[k], len(a)//2)#print для проверки
s1 = s2 = 0
s1 += t[39426]*39426#39426 - середина списка, и чтобы не считтаь его дважды
print(a[k])
for i in range(1, 39426):
    s1 += t[i]*i+t[-i]*i

print(s1)
k += 1
t1 = a[:k-1]
t2 = a[k-1:]
t = t2 + t1
print(len(t), t[0], len(a), a[k])
s2 += t[39426]*39426
for i in range(1, 39426):
    s2 += t[i]*i + t[-i]*i
print(s1, s2, abs(s1-s2))
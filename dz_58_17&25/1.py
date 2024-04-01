f = open('2__1n2uq.txt')
a = [int(i) for i in f]
t = [x for x in a if (x % 3 == 0) and (x % 7 != 0) and (x % 19 != 0) and (x % 17 != 0) and (x % 27 != 0)]
print(len(t), max(t))
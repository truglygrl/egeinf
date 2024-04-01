f = open('17__1vl6r.txt')
a = [int(i) for i in f]
t = [x for x in a if ((x % 10 == 3) or (x % 10 == 5)) and (x % 7 == 0)]
print(len(t), min(t))
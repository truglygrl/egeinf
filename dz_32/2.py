k=0
f = open('17__1jdyy.txt')
a = [int(i) for i in f]
sr = sum(a) / len(a)
mx = -100000000
x = 0
y = 0
for i in range(len(a)-1):
    t1 = int((a[i] < sr) + (a[i+1] < sr))
    t2 = int(('1' not in str(a[i])) + ('1' not in str(a[i+1])))
    if (t1 >= 1) and (t2 == 2):
        k += 1
        if (a[i] + a[i + 1]) > mx:
            x = a[i]
            y = a[i + 1]
            mx = a[i] + a[i + 1]
print(k, x, y)

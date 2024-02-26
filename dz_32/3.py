k = 0
mn = 10000000000000
f = open('17_4__1kacf.txt')
a = [int(i) for i in f]
for i in range(len(a)-1):
    t1 = [int(x) for x in str(a[i]) if int(x) % 2 == 0]
    t2 = [int(x) for x in str(a[i+1]) if int(x) % 2 == 0]
    if (len(t1) == len(str(a[i]))) and (len(t2) == len(str(a[i+1]))):
        print(a[i], a[i+1])
        k += 1
        mn = min(mn, a[i] + a[i+1])
print(k, mn)
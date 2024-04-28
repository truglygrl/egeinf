f = open('17__1sso1.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(len(a)-2):
    for j in range(i+2, len(a)):
        if (a[i] + a[j]) % 2 != 0 and a[i] > 0 and a[j] > 0:
            for k in range(i, j+1):
                if a[k] == 0:
                    c += 1
                    break

print(c)
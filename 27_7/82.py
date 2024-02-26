f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/8b.txt')
n = int(f.readline())
k = 98
mx1 = [-100]*k
mx2 = [-100]*k
ms = -1
ms1 = 0
x = int(f.readline())
for i in range(n-1):
    if x > mx1[x%k]:
        mx1[x%k] = x
    if (mx1[x%k] > x) and (x > mx2[x%k]):
        mx2[x%k] = x
    x = int(f.readline())
    t = (k - x % k) % k
    if ((x + mx1[t]) > ms) or ((x + mx2[t]) > ms) or ((mx1[t] + mx2[x%k]) > ms) or ((mx1[x%k] + mx2[t]) > ms):
        ms = max(ms, (x + mx1[t]), (x + mx2[t]), (mx1[t] + mx2[x%k]), (mx1[x%k] + mx2[t]))


print(max(mx1))
print(max(mx2))
print(ms - ms1, ms1)
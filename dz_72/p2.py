f = open('26-130__3cldm.txt')
n = int(f.readline())
stat = [0]*1440
for i in range(n):
    a, b = map(int, f.readline().split())
    for j in range(a, b+1):
        stat[j] += 1
print(stat.index(max(stat)))
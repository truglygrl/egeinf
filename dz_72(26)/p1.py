f = open('26-128__3cldl.txt')
n = 991
a = [list(map(int, i.split())) for i in f]
hall = [a[0][1]]
for i in range(991):
    if a[i][0] >= hall[-1]:
        hall.append(a[i][1])
        print(hall)
print(len(hall))
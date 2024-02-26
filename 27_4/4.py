f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/4a.txt')
n = int(f.readline())

counter = 0
prop = [0] * 13
a = int(f.readline())
for i in range(n-1):
    prop[0] += int(a % 5 == 0)
    prop[1] += int(a % 5 == 1)
    prop[2] += int(a % 5 == 2)
    prop[3] += int(a % 5 == 3)
    prop[4] += int(a % 5 == 4)
    prop[5] += int(a % 5 == 5)
    prop[6] += int(a % 5 == 6)
    prop[7] += int(a % 5 == 7)
    prop[8] += int(a % 5 == 8)
    prop[9] += int(a % 5 == 9)
    prop[10] += int(a % 5 == 10)
    prop[11] += int(a % 5 == 11)
    prop[12] += int(a % 5 == 12)

    y = int(f.readline())
    a = y
    if y % 13 == 0:
        counter += prop[0]
    elif y % 13 == 1:
        counter += prop[12]
    elif y % 13 == 2:
        counter += prop[11]
    elif y % 13 == 3:
        counter += prop[10]
    elif y % 13 == 4:
        counter += prop[9]
    elif y % 13 == 5:
        counter += prop[8]
    elif y % 13 == 6:
        counter += prop[7]
    elif y % 13 == 7:
        counter += prop[6]
    elif y % 13 == 8:
        counter += prop[5]
    elif y % 13 == 9:
        counter += prop[4]
    elif y % 13 == 10:
        counter += prop[3]
    elif y % 13 == 11:
        counter += prop[2]
    elif y % 13 == 12:
        counter += prop[1]

print(counter)
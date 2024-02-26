f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/3b.txt')
n = int(f.readline())

counter = 0
prop = [0] * 5
a = int(f.readline())
for i in range(n - 1):
    print(a)
    prop[0] += int(a % 5 == 0)
    prop[1] += int(a % 5 == 1)
    prop[2] += int(a % 5 == 2)
    prop[3] += int(a % 5 == 3)
    prop[4] += int(a % 5 == 4)
    print(prop)
    print(a % 5 == 0)

    y = int(f.readline())
    a = y
    print(a)
    if y % 5 == 0:
        counter += prop[0]
    elif y % 5 == 1:
        counter += prop[4]
    elif y % 5 == 2:
        counter += prop[3]
    elif y % 5 == 3:
        counter += prop[2]
    else:
        counter += prop[1]
    print(prop)
print(counter)
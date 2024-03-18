for a in range(500):
    fl = 0
    for x in range(1, 500):
        for y in range(1, 500):
            if (((y*y <= a) <= (y <= 10)) and ((x <= 9) <= (x*x < a))) == False:
                fl = 1
                break
            if fl == 1:
                break
    if fl == 0:
        print(a)
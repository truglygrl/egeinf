for x in range(21100, 28503):
    if (x % 71 == 0) and (x % 17 == 0) and (x % 13 != 0) and (x % 31 != 0):
        print(x)
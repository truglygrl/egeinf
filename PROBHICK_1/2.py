for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    if (((x <= y) and (z != w)) <= (u == (x or z))) == False:
                        print(x, y, z, w, u)

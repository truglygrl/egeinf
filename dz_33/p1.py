for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(y) or x) or (not (z) and w)) == (w == x):
                    print(x, y, z, w)
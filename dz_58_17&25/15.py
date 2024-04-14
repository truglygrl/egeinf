pfac = [39916800]
pfib = [39088169, 63245986, 102334155, 165580141]


mn = 10**20
for fc in pfac:
    for fb in pfib:
        if abs(fc - fb) == 828631:
            print(fc, fb)
print(mn)
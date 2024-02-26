a1 = '0123456789abc'
a2 = '0123456789abcefgh'
for x in range(13):
    for y in range(13):
        for x2 in range(17):
            for y2 in range(17):
                s1 = 13**4+x*13**3+4*13**2+1*13+y
                s2 = 6*17**5 + 7*17**4 + x2*17**3 + 3*17**2 + 2*17**1 + y2
                summ = s1+s2
                if (summ % 81 == 0) and (x == x2) and (y == y2):
                    print(summ, x, y, x2, y2)
                    print(summ//81)


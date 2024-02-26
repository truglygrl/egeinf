def RectPS(x1, y1, x2, y2):
    a = x2-x1
    b = y2-y1
    s = a*b
    p = (a+b)*2
    print("S =", s, "P =", p)

RectPS(int(input()), int(input()), int(input()), int(input()))

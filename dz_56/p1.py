from turtle import *
m = 20
for i in range(2):
    forward((10*m))
    right(90)
    forward((18*m))
    right(90)

pu()
forward((5*m))
right(90)
forward(7*m)
left(90)
pd()
for i in range(2):
    forward((10*m))
    right(90)
    forward((7*m))
    right(90)

pu()

for x in range(20):
    for y in range(20):
        goto(x*m, -y*m)
        dot(3)
done()

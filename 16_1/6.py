f= [0] *20
for n in range(3, 20, 3):
    f[n] = f[n//3]
print(f)


for n in range(20):

    if n <=1:
        f[n] = n

    elif (n>1) and (n% 3 != 0):
        f[n] = n + f[n+2]
    print(f)
print(f[17])
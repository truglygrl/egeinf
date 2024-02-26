f = [0]*10
for n in range(-2, 10):
    if n <=3:
        f[n] = 1
    else:
        f[n] = f[n//3] + f[n-1] + 2
    print(f)
print(f[7])
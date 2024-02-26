f = [0]*1000
for n in range(1000):
    if n <=2:
        f[n] = 1
    else:
        f[n] = (2*n + 7)*f[n-2]
print(f[8])
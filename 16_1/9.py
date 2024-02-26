f = [0]*20
f[1] = 3
f[2] = 6
f[3] = 9
for n in range(4, 20):
    f[n] = f[n-3]*n+2
    print(f)
print(f[12])
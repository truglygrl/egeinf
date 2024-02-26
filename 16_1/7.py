f = [2] * 10
for n in range(3, 10):
    f[n] = f[n-1]*(n*n+5)-4*n
    print(f)
print(f[5]/f[3])
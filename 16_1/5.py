f = [0]*100
for n in range(1, 100):
    if n <=5:
        f[n] = n*n + 5
    else:
        f[n] = f[n-2] + n*n - 3
    print(f)
print(f[7])
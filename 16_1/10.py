f = [0] * 10
f[0] = 1
f[1] = 2
for n in range(2, 10):
    f[n] = 6*f[n-1] - f[n-2]*n
    print(f)
print(f[4])
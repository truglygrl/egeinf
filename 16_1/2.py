f = [0]*11
f[1] = f[2] = f[3] = 1
for n in range(4, 11):
    f[n] = f[n-1] * 3 - f[n-3]

print(f)
print(f[10])
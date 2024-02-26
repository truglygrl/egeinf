f = [0] *102
f[100] = 102
f[101] = 103
for n in range(99, 0, -1):
    f[n] = 5 + n +f[n+2]
    print(f)
print(f[90] - f[101])

f = [0]*2025
for n in range(2025):
    if n < 7:
        f[n] = 7
    else:
        f[n] = n + 1 + f[n-2]

print(f[2024] - f[2020])
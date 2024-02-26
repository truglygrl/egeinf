f =[0]*20
for n in range(-10, 20):
    if n <=2:
        f[n] = 1
    else:
        f[n] = f[n-1]*n+f[n-5]*5
    print(f)
print(f[15])
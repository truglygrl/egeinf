f = open('1B__2rcsr.txt')
n = int(f.readline())
mn = []
mc = []
mx = -10
x = int(f.readline())
for i in range(n-1):
    if x % 2 == 0:
        mc.append(x)
    else:
        mn.append(x)
    x = int(f.readline())
    if x % 2 == 0:
        mx = max(mx, x*max(mc), x*max(mn))
    else:
        mx = max(mx, x*max(mc))
print(mx)

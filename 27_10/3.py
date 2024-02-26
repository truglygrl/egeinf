f = open('3B__2rct1.txt')
n = int(f.readline())
ans = 0
kr = [0]*9

for i in range(n):
    x = int(f.readline())
    for j in range(9):
        if (x + j) % 9 != 0:
            ans += kr[j]
    kr[x % 9] += 1

print(ans)

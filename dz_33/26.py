ans = 0
for x in range(121):
    s1 = 5*121**4 + 6*121**3 + 1*121**2 + x*121 + 4
    s2 = 1*121**4 + x*121**3 + 2*121**2 + 9*121
    if (s1 + s2) % 17 == 0:
        ans += (s1+s2) // 17
print(ans)
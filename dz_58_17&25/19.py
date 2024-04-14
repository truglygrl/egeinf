mn = min(x for x in range(100000, 300001) if (x % 13 == 0) and (x % 71 != 0))
mx = max(x for x in range(100000, 300001) if (x % 13 == 0) and (x % 71 != 0))
print(mn % 13,mx)
k = 0
s = set()
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            aq = ''.join(sorted(str(a) + str(b) + str(c)))
            s.add(aq)

print(s)
print(len(s))
for i in s:
    if sum(map(int, i)) == 6:
        print(i)
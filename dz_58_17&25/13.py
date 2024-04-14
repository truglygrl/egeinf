c = 0
for x in range(28585, 28801):
    if str(x)[-2] == '8':
        c += 1
print(c)
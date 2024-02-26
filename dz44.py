summ = 0
for i in range(1012, 9639):
    if i % 7 == 0 and str(i)[-1] == '1':
        summ+=i

print(summ)
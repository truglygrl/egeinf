n = list(map(int, input().split(' ')))
k = int(input())
l = int(input())

summ = 0

for i in range(len(n)):

    if i > k and i <= l:#в задании указано что нужно исключить
        # все эелементы массива кроме k и l включительно,
        # и не указано k включительно или нет,
        # если же k включительно, то будет
        # if i >= k and i <= l и в ответе в примере будет 24,
        # так как не будет учитываться n[k] = 3
        summ = summ
    else:
        summ += n[i]

print(summ)

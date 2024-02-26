for n in range(123123, 143124):
    for i in range(2, int(n**0.5)+1):
        if (n% i == 0) and ((n // i) == i):
            print(n)
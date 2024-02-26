

def SumRange(A, B):
    summ = 0
    if A < B:
        for i in range(A, B+1):
            summ += i
        print(summ)
    else:
        print(0)

SumRange(int(input()), int(input()))


for x in range(152346, 957813):
    t = set()
    if x**0.5 == int(x**0.5):

        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                t.add(i)
                t.add(x // i)
    if len(t) == 3:
        print(x, max(t))
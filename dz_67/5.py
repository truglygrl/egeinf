def f(n):
    if n >= 256:
        return n
    return 2*f(n+3) - f(n+4) + 3*n

print(f(8800)/f(250))
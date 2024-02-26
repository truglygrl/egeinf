s = '0' + 216*'1'
while '01' in s:
    if '0111' in s:
        s = s.replace('0111', '101', 1)
    else:
        s = s.replace('01', '10', 1)
print(s)
print(sum(int(i) for i in s))
n = int(s, 2)
print(n)
def f(x):
    s1 = ''
    while x > 0:
        s1 = str(x%8) + s1
        x = x // 8
    return int(s1)
print(f(n))
print(sum(int(j) for j in str(f(n))))
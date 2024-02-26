s = 'aaaaaQWaaaaQWaaaaaaaQWaaaa'
s = s.replace('QW', 'Q W')
print(s)
t = s.split()
n = [len(x) for x in t]
print(t)
print(n)
print(max(n))
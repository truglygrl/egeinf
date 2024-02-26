s = 'aaaaZaaaaaZaaaaaaaaaaaaaaaaZZZaaaZaaaaaaZaaaaaaaZaaaaaaaZaaaaaaaaaZaaaaaaZaaaa'
s = s.split('Z')
print(s)
t = list(map(len, s))
print(t)
mn = len(s) + 50
for i in range(len(t)-4):
    sm = sum(t[i:i+4])+5
    if sm < mn:
        mn = sm
print(mn)

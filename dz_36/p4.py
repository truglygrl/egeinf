s = open('24-210__2pt9q.txt').readline()
l = lm = 0
a = ['ABC', 'BAC', 'CAB', 'CBA']
for i in range(1, len(s)-2, 2):
    if s [i:i+3] in a:
        l += 1
        lm = max(l, lm)
    else:
        l = 0
print(lm)
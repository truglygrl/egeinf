s = open('24_3__28ylr.txt').readline().split('KK')
t = [len(x) for x in s if 'FM' in x]
print(max(t))
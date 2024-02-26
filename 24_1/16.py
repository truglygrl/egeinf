f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/16.txt')
s = f.readline()
#s = 'ssssUDsUFsUFsssssUDsUFsUFsssssUDsUFsUFs'
s = s.replace('AC', '**').replace('AD', '**').replace('AF', '**').replace('UC', '**').replace('UD', '**').replace('UF', '**')
print(s)
s = s.split('**')
print(s)
t = list(map(len, s))
print(t)
mx = 0
for i in range(len(t)-4):
    sm = sum(t[i:i+4]) + 6
    if sm > mx:
        mx = sm
print(mx)
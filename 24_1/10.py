f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/10.txt')
s = f.readline()
#s = 'DDDEEBDDCDCBCDBABDEDAdffhskjdfhksjdhfkjsdkDDDACEddddddddddddddddddddCDBCDCCAACDEDDEED'
s = s.replace('A', ' A')
s = s.replace('D', 'D ')
s = s.split()
print(s)
#DDDEEBDDCDCBCDB', 'BDEDDDDCECDBCDCC', '', 'CDEDDEED'
t = list(map(len, s))
print(t)
c = 0
for k in t:
    if k >= 10:
        c += 1
print(c)
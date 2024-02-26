s = '5'*60+'4'*30+'2'*90+'7'*120
while ('54' in s) or ('27' in s):
    if '55' in s:
        s = s.replace('55', '2', 1)
    elif '22' in s:
        s = s.replace('22', '7', 1)
    if '44' in s:
        s = s.replace('44', '4', 1)
    elif '77' in s:
        s = s.replace('77', '7', 1)
x = int(s)
summ = 0
while x > 0:
    summ += x%10
    x = x // 10
print(summ)
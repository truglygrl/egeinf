s = input()
if s[0] == 'x':
    if s[1] == '+':
        print(int(s[4]) - int(s[2]))
    elif s[1] == '-':
        print(int(s[4]) + int(s[2]))
elif s[2] == 'x':
    if s[1] == '+':
        print(int(s[4]) - int(s[0]))
    else:
        print(int(s[0]) - int(s[4]))
elif s[4] == 'x':
    if s[1] == '+':
        print(int(s[0]) + int(s[2]))
    elif s[1] == '-':
        print(int(s[0]) - int(s[2]))
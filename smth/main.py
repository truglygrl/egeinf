s = input()
stack = []
a = 'yes'
for i in s:
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
    elif stack:
        if i == ']' and stack[-1] == '[':
            del stack[-1]
        elif i == '}' and stack[-1] == '{':
            del stack[-1]
        elif i == ')' and stack[-1] == '(':
            del stack[-1]
if len(stack) == 0:
    a = 'yes'
else:
    a = 'no'

print(a)
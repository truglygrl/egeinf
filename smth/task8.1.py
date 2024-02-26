s = input()
a = 0
for word in s:
    if word in 'qwertyuiopasdfghjklzxcvbnmабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        a+=1
print(a)
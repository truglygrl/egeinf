f = open('3A__2ui78.txt')
n = int(f.readline())
# Список с суммами с разными остатками.
# Изначально суммы пустые.
m = [0]*1
for i in range(3):
    print(i, 'i')
    nums = list(map(int, f.readline().split()))
    print(nums, 'nums')
    # Собираем в отдельном списке суммы из всевозможных пар из тройки
    pairs = []
    for j in range(len(nums)):
        for k in range(j+1, len(nums)):
            pairs.append(nums[j]+nums[k])
    print(pairs, 'pairs')
    # Временный массив с суммами.
    m_new = [0] * 4
    print(m_new)
    # Перебор разных сумм со всеми суммами пар из тройки.
    # Суммы из m будут сравниваться между собой посредством условий.
    for t in range(4):
        for p in pairs:
            print(t, p, m[t] + p, m_new[(m[t] + p) % 4], 't, p, m[t] + p, m_new[(m[t] + p) % 4]')

            if m[t] + p > m_new[(m[t] + p) % 4]:
                m_new[(m[t] + p) % 4] = m[t] + p
                print(m, 'm')
                print(m_new, 'm_new')
    # Сохраняем получившийся массив в m
    m = m_new.copy()
    print(m, 'm mcopy')
# Просят максимальное, кратное 4.
# Значит выводим m[0]
print(m[0])
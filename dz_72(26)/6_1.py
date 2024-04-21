f = open('26__20xtp.txt')
n, load = map(int, f.readline().split())
all_cargo = sorted([int(x) for x in f], reverse=True)
print(n, load)
count = 0
while len(all_cargo):
    cargo = [all_cargo[0]]
    del(all_cargo[0])
    # Забираем самый тяжелый груз
    count += 1
    # Если есть грузы, которые поместятся еще на этот рейс, забираем и их
    vz = []
    for i in range(len(all_cargo)):
        if all_cargo[i] + sum(cargo) <= load:
            cargo += [all_cargo[i]]
            vz.append(i)
    # удаляем те грузы, которые только что забрали
    for i in range(len(vz)):
        x = vz[i] - i # вычитаем i так как после удаления очередного элемента индексация смещается
        #print(x, len(all_cargo))
        del(all_cargo[x])
    print(count, sum(cargo))
#print(count, cargo)
f = open('26_9__1vn9h.txt')
n = f.readline()
cubes = sorted([int(i) for i in f], reverse=True)
print(cubes)
cklad=[]
k = 0
while len(cubes)>0:
    #if k < 10:
        #print(k)
    block = [cubes.pop(0)]
    #print('block', block)
    for i in range(len(cubes)):
        if (block[-1]-cubes[i])>=3:
            block.append(cubes[i])
            cubes[i]=''
    #print('block', block)
    cubes=[x for x in cubes if x!='']
    #print('cubes', len(cubes))
    cklad.append(block)
    #print('cklad', [len(c) for c in cklad])
    k += 1
print(len(cklad),max(len(c) for c in cklad))
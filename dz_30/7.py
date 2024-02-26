s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
sa = 'AEYUOaeyouIi'
k = 0
for a in 'AEYUOaeyouIi':
    for b in s:
        for c in s:
            for d in '0123456789':

                k += 1
print(k)
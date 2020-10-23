n = 100
for i in range (1, n+1):
    summ = 0
    for j in range (1, 2*i):
        if j%2 != 0:
            summ = summ + j
    if summ == i*i:
        print(i, ': true')

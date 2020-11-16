n = int(input())
a = float(input())
number = 1
summ = a
while number<=n and a != 0:
    a = float(input())
    number = number + 1
    summ = summ + a
print (summ/number)

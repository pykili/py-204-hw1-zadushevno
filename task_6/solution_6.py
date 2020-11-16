n = int(input())
stupenka = ""
for i in range(n):
    stupenka = ""
    for j in range (i+1):
        k = str(j+1)
        stupenka = stupenka + k
    print(stupenka)

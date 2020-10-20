stroka = input()
alphabet = ""
for i in stroka:
    if (i in alphabet) == False:
        alphabet = alphabet + i
print(alphabet)

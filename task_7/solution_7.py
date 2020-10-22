stroka = input()
a = ""
is_palindrom = False
for i in stroka:
    a = i + a
if stroka == a:
    is_palindrom = True
print(is_palindrom)

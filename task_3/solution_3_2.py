alphabet = ""
for smth in 'a'*10:
    user_input = input ()
    for i in user_input:
        if (i in alphabet) == False:
            alphabet = alphabet + i
print(alphabet)

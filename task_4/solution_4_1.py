for smth in 'a'*10: #мне кажется я где-то запуталась и вообще можно было решить проще :с
    user_input = input()
    if user_input == "":
        pass
    else:
        if user_input[0] == '#':
            pass
        else:
            f1 = user_input.find('\t')
            f2 = user_input.find('\t', f1+1, len(user_input)-1)
            form = user_input[f1+1:f2]
            l1 = user_input.find('\t', f2+1, len(user_input)-1)
            lemma = user_input[f2+1:l1]
            my_cool_condition = lemma != form
            if my_cool_condition == True:
                print(form, lemma)

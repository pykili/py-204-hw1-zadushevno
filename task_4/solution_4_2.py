for smth in 'a'*10: 
    user_input = input()
    form = ""
    lemma = ""
    pos_t1 = 0
    pos_t2 = 0
    pos_t3 = 0
    count = 0
    if user_input == "":
        pass
    else:
        if user_input[0] == '#':
            pass
        else:
            for i in user_input:
                if i == '\t':
                    if pos_t1 == 0:
                        pos_t1 = count
                    else:
                        if pos_t2 == 0:
                            pos_t2 = count
                        else:
                            if pos_t3 == 0: 
                                pos_t3 = count
                count = count + 1
            symbol_pos = 0
            for j in user_input:
                if symbol_pos > pos_t1 and symbol_pos < pos_t2:
                    form = form + j
                if symbol_pos > pos_t2 and symbol_pos < pos_t3:
                    lemma = lemma + j
                symbol_pos = symbol_pos + 1
            symbol_pos = 0
            lemma_len = 0 
            for a in lemma:
                lemma_len = lemma_len + 1
            form_beginning = ""
            for i in form:
                if symbol_pos < lemma_len:
                    form_beginning = form_beginning + i
                symbol_pos = symbol_pos + 1
            if lemma != form_beginning:
                print(form, lemma) 
